

def solution(n):
    """Print number of consecutive 1s in binary representation of input
    number.

    Args:
        n (int): An integer in base 10 format.

    Side effects:
        Print number of consecutive 1s in the binary representation.
    """
    binary = bin(n)[2:]
    cnt = 0
    score = []
    for i in binary:
        if int(i) != 1:
            cnt = 0
        else:
            cnt += 1
        score.append(cnt)
    print(max(score))


if __name__ == '__main__':
    n = int(input())
    solution(n=n)
