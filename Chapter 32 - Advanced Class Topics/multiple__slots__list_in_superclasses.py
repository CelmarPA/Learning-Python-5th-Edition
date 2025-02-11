class E:
    __slots__ = ['c', 'd']                  # Superclass has slots

class D(E):
    __slots__ = ['a', '__dict__']           # But so does its subclass

X = D()

X.a = 1; X.b = 2; X.c = 3                   # The instance is the union (slots: a, c)

print(X.a, X.c)

print(E.__slots__)                          # But slots are not concatenated

print(D.__slots__)

print(X.__slots__)                          # Instance inherits *lowest* __slots__

print(X.__dict__)                           # And has its own an attr dict

for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))

print(dir(X))                               # But dir() includes all slot names
