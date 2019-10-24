import json
import re
from collections import defaultdict
from urllib.parse import urlencode

import scrapy

COUNTRIES = {
    "Australia": "AUS",
    "Austria": "AUT",
    "Bangladesh": "BGD",
    "Belgium": "BEL",
    "Canada": "CAN",
    "China": "CHN",
    "Denmark": "DNK",
    "Estonia": "EST",
    "Finland": "FIN",
    "France": "FRA",
    "Germany": "DEU",
    "Greece": "GRC",
    "Hong Kong": "HKG",
    "Ireland": "IRL",
    "India": "IND",
    "Indonesia": "IDN",
    "Italy": "ITA",
    "Luxembourg": "LUX",
    "Malaysia": "MYS",
    "Malta": "MLT",
    "Mexico": "MEX",
    "Nepal": "NPL",
    "Netherland": "NLD",
    "Pakistan": "PAK",
    "Philippines": "PHL",
    "Portugal": "PRT",
    "Singapore": "SGP",
    "Spain": "ESP",
    "Sri Lanka": "LKA",
    "Thailand": "THA",
    "UK": "GBR",
    "USA": "USA",
    "Vietnam": "VNM",
}

#
CURRENCIES = {
    "AUD": "AUS",
    "CAD": "CAN",
    "EUR": "DEU",
    "GBP": "GBR",
    "USD": "USA",
}


class Scraper(scrapy.Spider):

    name = "scraper"
    custom_settings = {}
    source_currencies = CURRENCIES.keys()
    pairs = defaultdict(set)

    def start_requests(self):
        query = {"source_currency": ",".join(self.source_currencies)}
        url = "https://www.instarem.com/api/v1/public/currency/pair?" + urlencode(query)
        yield scrapy.Request(
            url=url,
            callback=self.parse_pairs,
            headers={"X-Requested-With": "XMLHttpRequest"},
        )

    def parse_pairs(self, response):
        pair_data = json.loads(response.body)["data"]
        for source_currency, dest_currencies in pair_data.items():
            for currency in dest_currencies:
                self.pairs[source_currency].add(currency["destination_currency_code"])
        yield scrapy.Request(
            "https://www.instarem.com/en-au/au-sitemap",
            callback=self.parse_countries,
        )

    def parse_countries(self, response):
        query = '//div[text()="Send Money"]/following-sibling::div[1]//a'
        countries = response.xpath(query)
        for country in countries:
            yield response.follow(
                country,
                callback=self.parse_country,
                cb_kwargs={"dest_country": country.xpath("./text()").get()},
            )

    def parse_country(self, response, dest_country):
        match = re.search(r"dest_currency = '(.*?)';", response.body.decode())
        if not match:
            raise ValueError("No destination currency at " + response.url)
        dest_currency = match[1]
        for source_currency, dest_currencies in self.pairs.items():
            if dest_currency not in dest_currencies:
                continue
            yield {
                "source_country": CURRENCIES.get(source_currency, ""),
                "dest_country": COUNTRIES.get(dest_country, ""),
                "source_currency": source_currency,
                "dest_currency": dest_currency,
            }