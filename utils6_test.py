import pytest
from  utils import double

def test_zero():
	assert double(0) == 0, "Неверно для 0"

def test_one():
	assert double(1) == 2, "Неверно для 1"

def test_float():
	assert double(10.0) == 20.0, "Неверно для 10.0"

def test_negative():
	assert double(-3) == -6, "Неверно для -3"

def test_bigint():
    assert double(123456789) == 246913578, "Неверно для 123456789"