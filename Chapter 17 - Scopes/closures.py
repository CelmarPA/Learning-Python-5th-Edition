def maker(n):
    def action(x):      # Make and return action
        return x ** n       # action retains n from enclosing scope
    return action

f = maker(2)        # Pass 2 to argument n
print(f)
print(f(3))     # Pass 3 to x, n remembers 2: 3 ** 2
print(f(4))     # 4 ** 2

g = maker(3)        # g remembers 3, f remembers 2
print(g(4))     # 4 ** 3
print(f(4))     # 4 ** 2

def maker2(n):
    return lambda x: x ** n     # lambda functions retain state too

h = maker2(3)
print(h(4))     # 4 ** 3 again

def f1():
    x = 88
    def f2(x = x):      # Remember enclosing scope x with defaults
        print(x)
    f2()

f1()        # Prints 88

def f1():
    x = 88      # Pass x along instead of nesting
    f2(x)       # Forward reference OK

def f2(x):
    print(x)        # Flat is still often better than nested!

f1()
