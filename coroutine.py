def coroutine():
    while True:
        value = (yield)
        print(value)


routine = coroutine()
next(routine)

routine.send(8)
routine.send(4)
routine.send(True)

