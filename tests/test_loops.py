import pytest

from hrank._30_days_of_code._05_loops import solution


def test_loops(capsys):
    solution(n=2)
    assert capsys.readouterr().out == '2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n'
