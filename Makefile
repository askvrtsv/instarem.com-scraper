init:
	git init
	pipenv install --dev

clean:
	rm -f results/*.csv

scraper-dev: clean
	PYTHONPATH=$$(pwd) \
		SCRAPY_SETTINGS_MODULE=instarem.settings_dev \
		pipenv run scrapy crawl scraper -o results/items.csv --pdb

scraper: clean
	pipenv run scrapy crawl scraper -o results/items.csv
