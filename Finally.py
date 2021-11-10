def fun (a,b):
    try:
        if a > 0:
            return a + b
        else:
            raise ValueError

    execept ValueError:
        return 0
    finally:
        return -1
