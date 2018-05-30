

def solution(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n * i}')

if __name__ == '__main__':
    n = int(input())
    solution(n=n)
