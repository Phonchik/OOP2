def fun(a, b, c, d, *args, **kwargs):
    print(args)
    print(kwargs)
    print(a, b, c, d)
    return a + b


print(fun(3, 5, 7, 0, 12, 12315,))
print(fun(4, 8, 13, 169, 1, e=10))

data = (2, 7, 9, 4)
print(fun(*data))
print(*data, sep='___')
another = {'a' : 5, 'b' : 8, 'c' : 4, 'd' : 13}
print(fun(**another))