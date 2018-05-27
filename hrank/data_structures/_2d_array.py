import math
import os
import random
import re
import sys
from itertools import compress


class Hourglass:
    MASK = [[True, True, True],
            [False, True, False],
            [True, True, True]]

    def __init__(self, arr):
        self.arr = arr
        self.values = self.get_values(arr)

    def get_values(self, arr):
        h = [list(compress(d, s)) for d, s in zip(arr, self.MASK)]
        return [v for i in h for v in i]

    def sum(self):
        return sum(self.values)

    def __eq__(self, other):
        return self.values == other.values

    def __repr__(self):
        return f'Hourglass({self.arr})'


class Extractor:

    def __init__(self, arr):
        self.arr = arr
        self.cols = len(self.arr[0])
        self.rows = len(self.arr)

    def get_hourglasses(self):
        hourglasses = []
        for c in range(self.cols - 2):
            for r in range(self.rows - 2):
                sub_arr = [cc[r:r+3] for cc in self.arr[c:c+3]]
                hg = Hourglass(arr=sub_arr)
                hourglasses.append(hg)
        return hourglasses


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = Extractor(arr=arr).get_hourglasses()
    print([hg.values() for hg in hourglasses])
