import pytest
from utils6 import sum_of_two

def test0():
    assert sum_of_two(0, 0) == 0, "Неверно для 0 + 0"
def test1():
    assert sum_of_two(1, 1) == 2, "Неверно для 1 + 1"
def test2():
    assert sum_of_two(-10, 10) == 0, "Неверно для -10 + 10"