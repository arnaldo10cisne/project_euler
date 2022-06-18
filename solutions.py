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
    print('Problem 3')


def p4():
    print('Problem 4')
