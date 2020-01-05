from uw_py220_extras.lesson01 import math


def test_addit():
    total = math.addit(1, 2)
    assert total == 3


def test_subit():
    total = math.subit(9, 7)
    assert total == 2
