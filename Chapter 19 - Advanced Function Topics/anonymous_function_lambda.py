def func(x, y, z): return x + y + z

print(func(2, 3 ,4))

f = lambda x, y, z: x + y + z

print(f(2, 3 ,4))

x = (lambda a = 'fee', b = 'fie', c = 'foe': a + b + c)

print(x('wee'))

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)        # Title in enclosing def scope
    return action       # Return a function object

act = knights()
msg = act('Robin')      # 'robin' passed to x

print(msg)

print(act)      # act: a function, not its result

L = [lambda x: x ** 2,      # Inline function definition
     lambda x: x ** 3,
     lambda x: x ** 4]      # A list of three callable functions

for f in L:
    print(f(2))     # Prints 4, 8, 16

print(L[0](3))      # Prints 9

# The same as:

def f1(x): return x ** 2
def f2(x): return x ** 3        # Define named functions
def f3(x): return x ** 4

L = [f1, f2, f3]        # Define named functions

for f in L:
    print(f(2))     # Prints 4, 8, 16

print(L[0](3))      # Prints 9