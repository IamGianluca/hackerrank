from hrank.data_structures.arrays._2d_array import (
    Extractor,
    Hourglass,
)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglasses = Extractor(arr=arr).get_hourglasses()
    print(max([hg.sum() for hg in hourglasses]))
