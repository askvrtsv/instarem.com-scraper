import os

BOT_NAME = "instarem"

# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = True

COOKIES_DEBUG = False
COOKIES_ENABLED = False

CONCURRENT_REQUESTS = 5
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

DEPTH_PRIORITY = -1

# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

DOWNLOAD_DELAY = 0

DUPEFILTER_DEBUG = True

EXTENSIONS = {
}

HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = [401, 403, 500, 503]
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
HTTPCACHE_GZIP = False

# ITEM_PIPELINES = {
#    'instarem.pipelines.ProjectPipeline': 300,
# }

NEWSPIDER_MODULE = "instarem.spiders"

ROBOTSTXT_OBEY = False

# SPIDER_MIDDLEWARES = {
#    'instarem.middlewares.ProjectSpiderMiddleware': 543,
# }

SPIDER_MODULES = ["instarem.spiders"]

TELNETCONSOLE_ENABLED = False
TELNETCONSOLE_PORT = [6023]
TELNETCONSOLE_USERNAME = "scrapy"
TELNETCONSOLE_PASSWORD = "scrapy"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
)

# from instarem.utils import set_proxy
# set_proxy("http://localhost:8080")
