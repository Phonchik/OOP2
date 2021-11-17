from random import randint

numbers = [randint(-50,50) for

numbers.sort(key=lambda x: x**2)
print(*numbers)

print(*filter(lambla x: x >+ -10, numbers))