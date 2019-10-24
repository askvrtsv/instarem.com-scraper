import os


def set_proxy(proxy, types=("http_proxy", "https_proxy")):
    """"""
    for proxy_type in types:
        os.environ[proxy_type] = proxy
