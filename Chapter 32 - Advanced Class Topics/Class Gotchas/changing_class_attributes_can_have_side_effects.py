class X:
    a = 1                   # Class attribute

I = X()

print(I.a)

print(X.a)

X.a = 2                     # May change more than X

print(I.a)                  # I changes too

J = X()                     # J inherits from X's runtime values

print(J.a)                  # (but assigning to J.a changes a in J, not X or I)

class X: pass               # Make a few attribute namespaces

class Y: pass

X.a = 1                     # Use class attributes as variables
X.b = 2                     # No instances anywhere to be found
X.c = 3
Y.a = X.a + X.b + X.c

for X.i in range(Y.a): print(X.i)           # Prints 0..5

class Record: pass

X = Record()

X.name = 'Bob'

X.job = 'Pizza maker'

print(X.name, X.job)