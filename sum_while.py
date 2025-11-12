def sum(*args):
    result = 0
    i = 0
    while i < len(args):
        result = result + args[i]
        i = i + 1
    return result

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
