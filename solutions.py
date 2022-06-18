import math


def p1():
    sum = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    print(sum)


def p2():
    sum = 0
    a, b = 1, 2
    while b <= 4000000:
        if (b % 2 == 0):
            sum += b
        aux = b
        b = b + a
        a = aux
    print(sum)


def p3():
    def is_prime(num):
        for i in range(2, num - 1):
            if num % i == 0:
                return False
        return True

    number = 600851475143
    max_factor_possible = int(math.sqrt(number / 2))

    if max_factor_possible % 2 == 0:
        max_factor_possible += 1

    for i in range(max_factor_possible, 1, -2):
        if number % i == 0:
            if is_prime(i):
                print(f'Result: {i}')
                return


def p4():
    print('Problem 4')
