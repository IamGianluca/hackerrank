import pytest

from hrank._30_days_of_code._10_binary_numbers import solution


@pytest.mark.parametrize('input_,expected', [
    (0, '0\n'),      # binary: 0
    (5, '1\n'),      # binary: 101
    (13, '2\n'),     # binary: 1101
    (10000, '3\n'),  # binary: 10011100010000
    (11111, '3\n'),  # binary: 10101101100111
])
def test_solution(input_, expected, capsys):
    solution(input_)
    assert capsys.readouterr().out == expected
