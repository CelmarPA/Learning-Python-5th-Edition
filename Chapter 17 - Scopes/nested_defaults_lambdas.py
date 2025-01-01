def func():
    x = 4
    action = (lambda n: x ** n)     # x remembered from enclosing def
    return action

x = func()
print(x(2))     # Prints 16, 4 ** 2


def func1():
    x = 4
    action = (lambda n, x=x: x ** n)
    return action

x = func1()
print(x(2))     # Prints 16, 4 ** 2
