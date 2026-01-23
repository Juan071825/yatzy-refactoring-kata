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
    assert Yatzy.fives(*dice) == expected
    

@pytest.mark.parametrize("dice, expected", [
    [(4, 5, 4, 5, 4), 0],
    [(4, 4, 5, 5, 6), 6],
    [(4, 5, 6, 6, 6), 18],
])
def test_sixes_test(dice, expected):
    assert Yatzy.sixes(*dice) == expected
    


def test_one_pair():
    assert 6 == Yatzy().score_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy().score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy().score_pair(5, 3, 6, 6, 5)


def test_two_Pair():
    assert 16 == Yatzy().two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy().two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy().two_pair(3, 3, 6, 5, 4)


def test_three_of_a_kind():
    assert 9 == Yatzy().three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy().three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)


def test_four_of_a_knd():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy().smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy().largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
