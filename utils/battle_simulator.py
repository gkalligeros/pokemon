from typing import Dict

from models.pokemon import Pokemon, FightResult, BattleLogItem
import random
import copy


def calculate_starting_state(pokemon_one: Pokemon, pokemon_two: Pokemon) -> Dict[str, Pokemon]:
    if random.randint(0, 1) == 1:
        return {"attacker": pokemon_one, "defender": pokemon_two}
    return {"attacker": pokemon_two, "defender": pokemon_one}
    pass


def calculate_round(current_state: Dict[str, Pokemon], round_num: int) -> BattleLogItem:
    rnd = 2 * random.random()
    dmg = round(rnd * current_state['attacker'].attack, 1)
    return BattleLogItem(damage=dmg,
                         attacker=copy.deepcopy(current_state['attacker']),
                         defender=copy.deepcopy(current_state['defender']),
                         round=round_num)


def flip_state(current_state: Dict[str, Pokemon]) -> Dict[str, Pokemon]:
    return {"attacker": current_state['defender'], "defender": current_state['attacker']}


def simulate_fight(pokemon_one: Pokemon, pokemon_two: Pokemon) -> FightResult:
    current_round = 0
    current_state = calculate_starting_state(pokemon_one, pokemon_two)
    result = FightResult(log=[])
    while not is_battle_over(pokemon_one, pokemon_two):
        log_item = calculate_round(current_state, current_round)
        current_state['defender'].current_hp = round(current_state['defender'].current_hp - log_item.damage,2)

        result.log.append(log_item)
        current_state = flip_state(current_state)
        current_round += 1

    if pokemon_one.current_hp > 0:
        result.winner = pokemon_one
        result.loser = pokemon_two
    else:
        result.winner = pokemon_two
        result.loser = pokemon_one
    return result


def is_battle_over(pokemon_one, pokemon_two):
    return pokemon_one.current_hp <= 0 or pokemon_two.current_hp <= 0
