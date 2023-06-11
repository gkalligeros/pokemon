from typing import Dict, Any

from models.pokemon import Pokemon


def get_pokemon_model_from_api(api_data: Dict[str, Any]) -> Pokemon:
    ret = Pokemon()
    hp = [d for d in api_data['stats'] if d['stat']['name'] == 'hp'][0]['base_stat']
    attack = [d for d in api_data['stats'] if d['stat']['name'] == 'attack'][0]['base_stat']
    ret.max_hp = 10 * hp  # just to make sense
    ret.current_hp = ret.max_hp
    ret.name = api_data['name']
    ret.attack = attack
    return ret
