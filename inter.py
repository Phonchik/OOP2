numbers = [6, 7, 0]

iterator = iter(numbers)


while True:
    try:
        a = next(iterator)
        print(a)
    except StopInteration:
        break

for item in numbers:
    print(item)

        