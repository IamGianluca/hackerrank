import pytest

from hrank._30_days_of_code._06_review_loop import split


@pytest.mark.parametrize('string,expected', [
    ('Hacker', 'Hce akr\n'),
    ('Rank', 'Rn ak\n'),
    ('', ' \n')
])
def test_split(string, expected, capsys):
    split(string)
    assert capsys.readouterr().out == expected
