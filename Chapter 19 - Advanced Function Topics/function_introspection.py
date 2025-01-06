def func(a):
    b = 'spam'
    return b * a

print(func(8))

print(func.__name__)

print(dir(func))

print(func.__code__)

print(dir(func.__code__))

print(func.__code__.co_varnames)

print(func.__code__.co_argcount)