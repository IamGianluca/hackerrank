import pytest

from hrank.data_structures._2d_array import (
    Extractor,
    Hourglass
)


@pytest.mark.parametrize('arr,expected', [
    ([[1,2,3], [4,5,6], [7,8,9]], [1,2,3,5,7,8,9]),
    ([[9,0,0], [3,2,1], [0,1,4]], [9,0,0,2,0,1,4])
])
def test_hourglass_values(arr, expected):
    hg = Hourglass(arr)
    assert hg.values == expected


@pytest.mark.parametrize('arr,expected', [
    ([[1,2,3], [4,5,6], [7,8,9]], 35),
    ([[9,0,0], [3,2,1], [0,1,4]], 16)
])
def test_hourglass_sum(arr, expected):
    hg = Hourglass(arr)
    assert hg.sum() == expected


def test_hourglass_repr():
    hg = Hourglass([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
    assert repr(hg) == 'Hourglass([[1, 2, 3], [4, 5, 6], [7, 8, 9]])'


@pytest.mark.parametrize('arr,expected', [
    ([[1,1,1,0],
      [0,1,0,0],
      [1,1,1,0],
      [0,0,2,4]],
     [Hourglass([[1,1,1],
                 [0,1,0],
                 [1,1,1]]),
      Hourglass([[1,1,0],
                 [1,0,0],
                 [1,1,0]]),
      Hourglass([[0,1,0],
                 [1,1,1],
                 [0,0,2]]),
      Hourglass([[1,0,0],
                 [1,1,0],
                 [0,2,4]])])
])
def test_extractor(arr, expected):
    extractor = Extractor(arr=arr)
    assert extractor.get_hourglasses() == expected
