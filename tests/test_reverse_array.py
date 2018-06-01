import pytest

from hrank._30_days_of_code._07_arrays import reverse_array


# TODO: this doesn't work I believe due to a bug in pytest.
# See: https://github.com/pytest-dev/pytest/issues/3524
# @pytest.mark.parametrize('array,expected', [
    # ('0 1 2 3', '3 2 1 0\n'),
    # ('1 4 3 2', '2 3 4 1\n'),
# ])
# def test_reverse_array(array, expected, capsys):
    # reverse_array(array=array)
    # assert capsys.readouterr().out == expected
