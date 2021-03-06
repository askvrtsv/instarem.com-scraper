from instarem.settings import *

CLOSESPIDER_ERRORCOUNT = 0
CLOSESPIDER_ITEMCOUNT = 0
CLOSESPIDER_PAGECOUNT = 0
CLOSESPIDER_TIMEOUT = 0

COOKIES_DEBUG = True

CONCURRENT_REQUESTS = 1

DOWNLOAD_DELAY = .5

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60 * 24

from instarem.utils import set_proxy
set_proxy("http://localhost:8080")
