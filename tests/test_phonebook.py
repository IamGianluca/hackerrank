import pytest

from hrank._30_days_of_code._08_dictionaries_and_maps import phonebook


@pytest.mark.parametrize('input_,expected', [
    (['1', 'Mark 01234', 'Mark'], 'Mark=01234\n'),
    (['3', 'Mark 012', 'Luca 0000', 'Brig 7271', 'John', 'Jerome', 'Brig'],
     'Not found\nNot found\nBrig=7271\n'),
])
def test(input_, expected, monkeypatch, capsys):
    g = (i for i in input_)
    monkeypatch.setattr('builtins.input', lambda: next(g))
    phonebook()

    assert capsys.readouterr().out == expected
