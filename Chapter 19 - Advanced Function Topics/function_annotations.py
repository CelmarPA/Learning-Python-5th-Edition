def func(a, b, c):
    return a + b + c

print(func(1,2, 3))

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

print(func(1, 2, 3))

print(func.__annotations__)

def func(a: 'spam', b, c: 99):
    return a + b + c

print(func(1, 2, 3))

print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])

def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c

print(func(1, 2, 3))
print(func())
print(func(1, c = 10))

print(func.__annotations__)

def func(a:'spam'=4, b:(1, 10)=5, c:float=6)->int:
    return a+b+c

print(func(1, 2))

print(func.__annotations__)