from utils.battle_simulator import calculate_starting_state, calculate_round, is_battle_over, simulate_fight, flip_state
from models.pokemon import Pokemon


def test_simulate_fight_win_sure():
    one = Pokemon(name='test_1', max_hp=10, current_hp=10, attack=1)
    two = Pokemon(name='test_2', max_hp=10, current_hp=10, attack=100)
    res = simulate_fight(one, two)
    assert res.winner.name == 'test_2'
    assert res.loser.name == 'test_1'


def test_simulate_fight_win_not_sure():
    one = Pokemon(name='test_1', max_hp=10, current_hp=10, attack=1)
    two = Pokemon(name='test_2', max_hp=10, current_hp=10, attack=1)
    res = simulate_fight(one, two)
    assert (res.winner.name == 'test_2' or res.winner.name == 'test_1')
    assert (res.loser.name == 'test_1' or res.loser.name == 'test_2')


def test_calculate_starting_attacker():
    one = Pokemon()
    two = Pokemon()
    start = calculate_starting_state(one, two)
    assert (one == start['attacker'] and two == start['defender'] or (
            two == start['attacker'] and one == start['defender']))


def test_is_battle_over_one():
    one = Pokemon(current_hp=0)
    two = Pokemon(current_hp=1)
    assert is_battle_over(one, two) is True


def test_is_battle_over_two():
    one = Pokemon(current_hp=1)
    two = Pokemon(current_hp=0)
    assert is_battle_over(one, two) is True


def test_is_battle_not_over():
    one = Pokemon(current_hp=1)
    two = Pokemon(current_hp=1)
    assert is_battle_over(one, two) is False


def test_flip_state():
    one = Pokemon(name='test_1', max_hp=10, current_hp=10, attack=1)
    two = Pokemon(name='test_2', max_hp=10, current_hp=10, attack=100)

    start = calculate_starting_state(one, two)
    flipped = flip_state(start)
    assert start['attacker'].name == flipped['defender'].name


def test_calculate_round():
    one = Pokemon(name='test_1', max_hp=10, current_hp=10, attack=1)
    two = Pokemon(name='test_2', max_hp=10, current_hp=10, attack=100)

    log = calculate_round({'attacker': one, 'defender': two}, round_num=1)

    assert log.damage <= 2 * one.attack
    assert log.damage >= 0
