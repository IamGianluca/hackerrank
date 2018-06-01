

def reverse_array(array):
    print(' '.join(array[::-1]))


if __name__ == '__main__':
    n = input()
    array = input().split(' ')
    reverse_array(array=array)
