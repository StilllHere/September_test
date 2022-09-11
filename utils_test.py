import pytest
from utils import double

def test_double():
    assert double(2) == 4

def test_double2():
    assert double(100) == 200