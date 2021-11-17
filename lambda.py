from random import randint

numbers = [int(x) for x in input().split()]
numbers.sort(key=lambda x: x ** 2)
print(*filter(lambda x: x >+ -10, numbers))