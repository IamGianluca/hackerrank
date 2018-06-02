

def reverse_array(array):
    print(' '.join(array.split(' ')[::-1]))


if __name__ == '__main__':
    n = input()
    array = input()
    reverse_array(array=array)
