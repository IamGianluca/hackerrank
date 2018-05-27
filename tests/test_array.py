import pytest

from hrank.data_structures.arrays import reverse_array


@pytest.mark.parametrize('arr,expected', [
    ([1,2,3,10], [10,3,2,1]),
    ([0,0,-1,5], [5,-1,0,0])
])
def test_reverse_array(arr, expected):
    assert reverse_array(arr) == expected
