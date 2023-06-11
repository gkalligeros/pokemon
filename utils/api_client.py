from typing import Dict, Any, Optional

import requests

from config import config
from utils.cache import get_cache


def get_pokemon_data(name: str) -> Optional[Dict[str, Any]]:
    """Retrieve answer data from API"""
    cache = get_cache()

    key = cache.generate_key("get_pokemon_data", name)
    if not cache.in_cache(key):
        resp = requests.get(
            f"{config.POKEAPI_HOST}/pokemon/{name}",
        )
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        resp_json = resp.json()
        cache.store_json(key=key, value=resp_json)
        return resp_json
    return cache.get_json(key)



def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i: i + n]
