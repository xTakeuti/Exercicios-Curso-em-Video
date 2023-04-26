from math import factorial


def fatorial(x, show=False):
    y = factorial(x)
    print(y)
    if show == True:
        for x in range(x - 1):
            print(f'{x + 1} x ', end='')
    print(x + 2, end='')
    print(f' = {y}')


fatorial(8, show=True)
