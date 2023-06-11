from utils.api_client import get_pokemon_data
from utils.cache import RedisCache
from config import config

import string
import random
import json

config.CACHE_DRIVER = 'redis'

def test_store_json():
    cache = RedisCache()
    key, random_dict = store_dummy_payload(cache)
    assert cache.in_cache(key) == True
    assert json.dumps(cache.get_json(key)) == json.dumps(random_dict)

def test_del_json():
    cache = RedisCache()
    key, random_dict = store_dummy_payload(cache)
    assert cache.in_cache(key) == True
    assert json.dumps(cache.get_json(key)) == json.dumps(random_dict)
    cache.del_key(key)
    assert cache.get_json(key) is None


def store_dummy_payload(cache):
    name = random_str(5)
    random_dict = {}
    for _ in range(1, 5):
        random_dict[random_str(5)] = random_str(5)
    key = cache.generate_key("get_pokemon_data", name)
    cache.store_json(key, random_dict)
    return key, random_dict


def random_str(n: int):
    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=n))
