from models.pokemon import BattleItem
from utils.api_client import get_pokemon_data
from utils.api_parser import get_pokemon_model_from_api
from utils.battle_simulator import simulate_fight
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/api/v1/pokemon/battle")
async def root(pokemons: BattleItem):
    try:
        first_api_data = get_pokemon_data(pokemons.first_pokemon)
        second_api_data = get_pokemon_data(pokemons.second_pokemon)
    except Exception:
        raise HTTPException(status_code=500, detail=f"Internal error")

    if first_api_data is None:
        raise HTTPException(status_code=404, detail=f"Pokemon with name {pokemons.first_pokemon} not found")
    if second_api_data is None:
        raise HTTPException(status_code=404, detail=f"Pokemon with name {pokemons.second_pokemon} not found")

    one = get_pokemon_model_from_api(api_data=first_api_data)
    two = get_pokemon_model_from_api(api_data=second_api_data)
    res = simulate_fight(one, two)
    return res
