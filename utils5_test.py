import pytest
from utils5 import multiply

def test_mismatch_a():
    with pytest.raises(ValueError):
        multiply(10.0,0)

def test_mismatch_b():
    with pytest.raises(ValueError):
        multiply(0, 10.0)

def test_mismatch_both():
    with pytest.raises(ValueError):
        multiply(10.0, 5.0)