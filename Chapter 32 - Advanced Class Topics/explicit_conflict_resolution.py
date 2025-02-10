class A:                attr = 1                # Classic

class B(A):             pass

class C(A):             attr = 2

class D(B, C):          attr = C.attr           # <== Choose C, to the right

x = D()

print(x.attr)                                   # Works like new-style (all 3.X)

class A(object):        attr = 1                # New-style

class B(A):             pass

class C(A):             attr = 2

class D(B, C):          attr = B.attr           # <== Choose A.attr, above

x = D()

print(x.attr)                                   # Works like classic (default 2.X)

class A:
    def meth(s): print('A.meth')

class C(A):
    def meth(s): print('C.meth')

class B(A):
    pass

class D(B, C): pass                             # Use default search order

x = D()                                         # Will vary per class type

x.meth()                                        # Defaults to classic order in 2.X

class D(B, C): meth = C.meth                    # <== Pick C's method: new-style (and 3.X)

x.meth()

class B(B, C): meth = B.meth                    # <== Pick B's method: classic

x = D()

x.meth()
