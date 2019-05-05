import yaml
from pkg import module


def test_multiplication():
    assert module.multiply(3, 2) == 6



def test_divide():
    assert module.divide(6, 2) == 3
