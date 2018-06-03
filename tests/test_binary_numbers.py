import pytest

from hrank._30_days_of_code._10_binary_numbers import solution


@pytest.mark.parametrize('input_,expected', [
    (0, '0\n'),
    (5, '1\n'),
    (13, '2\n'),
    (10000, '3\n'),
    (11111, '3\n')
])
def test_solution(input_, expected, capsys):
    solution(input_)
    assert capsys.readouterr().out == expected
