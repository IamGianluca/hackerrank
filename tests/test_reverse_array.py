import pytest

from hrank._30_days_of_code._07_arrays import reverse_array


@pytest.mark.parametrize('array,expected', [
    ('0 1 2 3', '3 2 1 0\n'),
    ('1 4 3 2', '2 3 4 1\n'),
])
def test_reverse_array(array, expected, capsys):
    reverse_array(array=array)
    assert capsys.readouterr().out == expected
