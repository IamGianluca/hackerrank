

def split(string):
    length = len(string)
    odd = string[0:length:2]
    even = string[1:length:2]
    print(' '.join([odd, even]))


if __name__ == '__main__':
    n = input()

    strings = []
    for i in range(int(n)):
        split(input())
