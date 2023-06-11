from utils import api_parser


def test_get_pokemon_model_from_api():
    api_payload = {
        'name': 'babis',
        'stats': [
            {
                "base_stat": 90,
                "effort": 2,
                "stat": {
                    "name": "hp",
                    "url": "https://pokeapi.co/api/v2/stat/1/"
                }
            },
            {
                "base_stat": 55,
                "effort": 0,
                "stat": {
                    "name": "attack",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ]
    }
    pok = api_parser.get_pokemon_model_from_api(api_payload)
    assert pok.attack == 55
    assert pok.max_hp == 10*90
    assert pok.current_hp == 10*90
    assert pok.name == 'babis'
