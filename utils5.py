def multiply(a, b):
    if type(a) != int:
        raise ValueError("Аргументы должны быть int")
    elif type(b) != int:
        raise ValueError("Аргументы должны быть int")
    return a*b