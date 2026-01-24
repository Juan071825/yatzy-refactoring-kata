import pytest 
from src.yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/



@pytest.mark.parametrize("dices, expected", [
    ((2,3,4,5,1), 15),
    ((3,3,4,5,1), 16),
])
def test_chance_score_sum_dice(dices, expected):
    assert Yatzy.chance(*dices) == expected



@pytest.mark.parametrize("dice, expected", [
    ([4, 4, 4, 4, 4], 50),
    ([6, 6, 6, 6, 6], 50),
    ([6, 6, 6, 6, 3], 0),
])
def test_yatzy_scores_50(dice, expected):
    assert Yatzy.yatzy(dice) == expected


@pytest.mark.parametrize("dice, expected", [
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 1, 4, 5], 2),
    ([6, 2, 2, 4, 5], 0),
    ([1, 2, 1, 1, 1], 4),
])
def test_ones(dice, expected):
    assert Yatzy.ones(*dice) == expected


@pytest.mark.parametrize("dice, expected", [
    ([1, 2, 3, 2, 6], 4),
    ([2, 2, 2, 2, 2], 10),
])  
def test_two(dice, expected):
    assert Yatzy.twos(*dice) == expected 


@pytest.mark.parametrize("dice, expected", [
    ([1, 2, 3, 2, 3], 6),
    ([2, 3, 3, 3, 3], 12),
])
def test_threes(dice, expected):
    assert Yatzy.threes(*dice) == expected

@pytest.mark.parametrize("dice, expected", [
    ([4, 4, 4, 5, 5], 12),
    ([4, 4, 5, 5, 5], 8),
    ([4, 5, 5, 5, 5], 4),
])

def test_fours_test(dice, expected):
    assert Yatzy.fours(*dice) == expected

@pytest.mark.parametrize("dice, expected", [
    [(4, 4, 4, 5, 5), 10],
    [(4, 4, 5, 5, 5), 15],
    [(4, 5, 5, 5, 5), 20],
])
def test_fives(dice, expected):
    assert Yatzy.fives(dice) == expected
    

@pytest.mark.parametrize("dice, expected", [
    [(4, 5, 4, 5, 4), 0],
    [(4, 4, 5, 5, 6), 6],
    [(4, 5, 6, 6, 6), 18],
])
def test_sixes(dice, expected):
    assert Yatzy.sixes(dice) == expected
    
@pytest.mark.parametrize("dice, expected", [
    [(3, 4, 3, 5, 6), 6],
    [(4, 3, 3, 5, 5), 10],
    [(4, 5, 6, 6, 5), 12],
])
def test_score_pair(dice, expected):
    assert Yatzy.score_pair(*dice) == expected

@pytest.mark.parametrize("dice, expected", [
    [(3, 3, 5, 5, 4), 16],
    [(3, 3, 6, 6, 6), 18],
    [(3, 3, 6, 5, 4), 0],
])

def test_two_Pair(dice, expected):
    assert Yatzy.two_pair(*dice) == expected


@pytest.mark.parametrize("dice, expected", [
    [(3, 3, 3, 4, 5), 9],
    [(5, 3, 5, 4, 5), 15],
    [(3, 3, 3, 3, 4), 9],
])

def test_three_of_a_kind(dice, expected):
    assert Yatzy.three_of_a_kind(*dice) == expected

@pytest.mark.parametrize("dice, expected", [
    [(3, 3, 3, 3, 5), 12],
    [(5, 5, 5, 4, 5), 20],
    [(3, 3, 3, 3, 3), 12],
    [(3, 3, 3, 2, 1), 0],
])

def test_four_of_a_kind(dice, expected):
    assert Yatzy.four_of_a_kind(*dice) == expected

@pytest.mark.parametrize("dice, expected", [
    [(1, 2, 3, 4, 5), 15],
    [(2, 3, 4, 5, 1), 15],
    [(1, 2, 2, 4, 5), 0],
])

def test_smallStraight(dice, expected):
    assert Yatzy.smallStraight(*dice) == expected



@pytest.mark.parametrize("dice, expected", [
    [(6, 2, 3, 4, 5), 20],
    [(2, 3, 4, 5, 6), 20],
    [(1, 2, 2, 4, 5), 0],
])

def test_largeStraight(dice, expected):
    assert Yatzy.largeStraight(*dice) == expected

@pytest.mark.parametrize("dice, expected", [
    [(6, 2, 2, 2, 6), 18],
    [(2, 3, 4, 5, 6), 0],
])

def test_fullHouse(dice, expected):
    assert Yatzy.fullHouse(*dice) == expected