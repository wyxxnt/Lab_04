from functools import reduce


def sum(*args):
    def add(acc, value):
        return acc + value

    return reduce(add, args, 0)

a = sum(1, 2, 3)
print('a =', a)

b = sum(0)
print('b =', b)

c = sum()
print('c =', c)

d = sum(1, -1, 1)
print('d =', d)

e = sum(10, -1, -1, -1)
print('e =', e)
