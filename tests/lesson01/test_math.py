from uw_py220_extras.lesson01 import math


def test_addit():
    advanced_math = math.AdvancedMath("blah")
    total = advanced_math.addit("c", "a")
    assert total == "ca"


def test_subit():
    advanced_math = math.AdvancedMath("more blah")
    total = advanced_math.subit(9, 7)
    assert total == 2
