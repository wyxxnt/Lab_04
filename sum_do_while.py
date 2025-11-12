def sum(*args):
    result = 0
    if len(args) == 0:
        return result
    i = 0
    while True:
        result = result + args[i]
        i = i + 1
        if i >= len(args):
            break
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
