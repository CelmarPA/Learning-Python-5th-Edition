class A: pass

class B(A): pass                    # Diamonds: order differs for newstyle

class C(A): pass                    # Breadth-first across lower levels

class D(B, C): pass


print(D.__mro__)

class A: pass

class B(A): pass                    # Nondiamonds: order same as classic

class C: pass                       # Depth first, then left to right

class D(B, C): pass

print(D.__mro__)

class A: pass

class B: pass                       # Another nondiamond: DFLR

class C(A): pass

class D(B, C): pass

print(D.__mro__)

print(A.__bases__)                  # Superclass links: object at two roots

print(B.__bases__)

print(C.__bases__)

print(D.__bases__)

class X: pass

class Y: pass

class A(X): pass                    # Nondiamond: depth first then left to right

class B(Y): pass                    # Though implied "object" always forms a diamond

class D(A, B): pass

print(D.mro())

print(X.__bases__, Y.__bases__)

print(A.__bases__, B.__bases__)

print(D.mro() == list(D.__mro__))

print([cls.__name__ for cls in D.__mro__])
