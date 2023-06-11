from typing import List, Optional

from pydantic import BaseModel


class BattleItem(BaseModel):
    first_pokemon: str
    second_pokemon: str


class Pokemon(BaseModel):
    name: Optional[str]
    max_hp: Optional[int]
    current_hp: Optional[float]
    attack: Optional[int]


class BattleLogItem(BaseModel):
    damage: float
    round: int
    attacker: Pokemon
    defender: Pokemon


class FightResult(BaseModel):
    winner: Optional[Pokemon]
    loser: Optional[Pokemon]
    log: List[BattleLogItem]
