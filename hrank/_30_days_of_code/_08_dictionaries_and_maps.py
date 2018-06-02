

def phonebook():
    n = int(input())

    phonebook = dict()
    for i in range(n):
        name, number = input().split(' ')
        phonebook[name] = number

    for i in range(n):
        name = input()
        try:
            print(f'{name}={phonebook[name]}')
        except KeyError:
            print('Not found')


if __name__ == '__main__':
    phonebook()
