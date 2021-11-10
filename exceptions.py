def divide(a, b):
    return a / b


try:
    x, y = [int(x) for x in input().split()]
    result = divide(x, y)
    print(result)
except ZeroDivisionError:
    print("Делить на ноль незья")
except ValueError as error:
    print("Неверный тип данных")
    print(error)