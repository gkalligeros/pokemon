import datetime
from os import  getenv

POKEAPI_HOST = "https://pokeapi.co/api/v2/"
REDIS_HOST = getenv("REDIS_HOST", "localhost")
REDIS_USER = getenv("REDIS_USER", None)
REDIS_PASSWORD = getenv("REDIS_PASSWORD", None)

CACHE_DRIVER = getenv("CACHE_DRIVER", 'redis')

CACHE_LIFETIME = datetime.timedelta(days=1)
