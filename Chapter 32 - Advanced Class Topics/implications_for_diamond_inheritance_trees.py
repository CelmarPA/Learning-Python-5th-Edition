class A(object):        attr = 1                    # New-style ("object" not required in 3.X)

class B(A):     pass

class C(A):     attr = 2                    # Tries C before A

class D(B, C):  pass

x = D()
print(x.attr)                               # Searches x, D, B, C
