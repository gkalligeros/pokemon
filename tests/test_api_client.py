from utils.api_client import get_pokemon_data
from fastapi import FastAPI, Depends


def test_non_existing():
    pok = get_pokemon_data("nonexisting")
    assert pok is None


def test_existing():
    pok = get_pokemon_data("ditto")
    assert pok is not None
    assert type(pok) is dict
