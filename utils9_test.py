import pytest
from utils6 import sum_of_two

@pytest.mark.parametrize(
	"first, second, expected",
	[(0, 0, 0), (1, 1, 2),(-10, 10, 0)]
)
def test_sum_of_two(first, second, expected):
    assert sum_of_two(first, second) == expected