X = 1
L = [1 , 2]

def changer(a, b):
    a = 2
    b[0] = 'spam'

changer(X, L[:]) # Pass a copy, so our 'L' does not change

print(X, L)

def changer(a, b):
    b = b[:]        # Copy input list so we don't impact caller
    a = 2
    b[0] = 'spam'   # Changes our list copy only

changer(X, L)

print(X, L)

changer(X, tuple(L))
