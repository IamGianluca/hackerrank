import pytest

from hrank._30_days_of_code._09_factorial import factorial


@pytest.mark.parametrize('n,expected', [
    (3, 6),
    (1, 1),
    (5, 120)
])
def test_factorial(n, expected):
    assert factorial(n) == expected
