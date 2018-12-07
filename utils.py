import importlib
import requests
def get_store_class_by_name(store_class_name):
    store_module = importlib.import_module('tiendas')
    return getattr(store_module, store_class_name)

def session_with_proxy(extra_args):
    session = requests.Session()

    if extra_args and 'proxy' in extra_args:
        proxy = extra_args['proxy']

        session.proxies = {
            'http': proxy,
            'https': proxy,
        }

    return session
