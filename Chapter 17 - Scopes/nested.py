X = 99      # Global scope name: not used

def f1():
    X = 88      # Enclosing def local
    def f2():
        print(X)        # Reference made in nested def
    f2()

f1()        # Prints 88: enclosing def local

def f3():
    X = 88
    def f4():
        print(X)        # Remembers X in enclosing def scope
    return f4()         # Return f2 but don't call it

action = f3()   # Make, return function
