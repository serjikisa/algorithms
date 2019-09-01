import sys
import datetime
from functools import lru_cache

cache = {}

def fibo01(n):
    '''
    recursive, global cache defined
    Limited, there is a max recursion
    '''
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        value = 1
    else:
        value = fibo(n - 1) + fibo(n - 2)

    cache[n] = value
    return value

@lru_cache(maxsize = 1000)
def fibo02(n):
    '''
    recursion with lru_cache
    clear implementation, max recursion still a limitation
    '''
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibo3(n-1) + fibo3(n-2)

def fibo03(n):
    '''
    dynamic programming
    '''
    answers = [1, 1]

    while len(answers) < n:
        answers.append(answers[-1] + answers[-2])

    return answers[n - 1]


def fibo04(n):
    '''
    dynamic programming, with O(1) size of array
    most efficient and faster for big inputs
    '''
    answers = [1, 1]
    for i in range(2, n):
        answers.append(answers[-1] + answers[-2])
        answers.pop(0)

    return answers[-1]

if __name__ == "__main__":
    n = int(sys.argv[1])
    # for i in range(1, n + 1):
    t1 = datetime.datetime.now()
    # a = fibo_big(i, 950)
    a = fibo04(n)
    td1 = datetime.datetime.now() - t1
    t2 = datetime.datetime.now()
    b = fibo03(n)
    td2 = datetime.datetime.now() - t2
    if a == b:
        print(a)
    else:
        print('Error')
    print(td1, 'Fibo04 seconds')
    # print(b)
    print(td2, 'Fibo03 seconds')
