def f(a):       # a is assigned to (references) the passed object
    a = 99      # Changes local variable a only

b = 88
f(b)        # a and b both reference same 88 initially
print(b)    # b is not changed

def changer(a, b):  # Arguments assigned references to objects
    a = 2       # Changes local name's value only
    b[0] = 'spam'       # Changes shared object in place

X = 1
L = [1, 2]      # Caller:
changer(X, L)       # Pass immutable and mutable objects

print(X, L)     # X is unchanged, L is different!

