from symtable import Class


class X:
    def m(self): print('X.m')

class Y:
    def m(self): print('Y.m')

class C(X):                                         # Start out inheriting from X
    def m(self): super().m()                        # Can't hardcode class name here

i = C()

i.m()

C.__bases__ = (Y,)                                  # Change superclass at runtime!

i.m()

class C(X):
    def m(self): C.__bases__[0].m(self)             # Special code for a special case

i = C()

i.m()

C.__bases__ = (Y,)

i.m()

# The basics: Cooperative super call in action

class B:
    def __init__(self): print('B.__init__')          # Disjoint class tree branches

class C:
    def __init__(self): print('C.__init__')

class D(B, C): pass

x = D()                                              # Runs leftmost only by default

class D(B, C):
    def __init__(self):                              # Traditional form
        B.__init__(self)                             # Invoke supers by name
        C.__init__(self)

x = D()

print('-' * 80)

class A:
    def __init__(self): print('A.__init__')

class B(A):
    def __init__(self): print('B.__init__'); A.__init__(self)

class C(A):
    def __init__(self): print('C.__init__'); A.__init__(self)

x = B()

x = C()                                               # Each super works by itself

class D(B, C): pass                                   # Still runs leftmost only

x = D()

class D(B,C):
    def __init__(self):                               # Traditional form
        B.__init__(self)                              # Invoke both supers by name
        C.__init__(self)

x = D()                                               # But this now invokes A twice

print('-' * 80)

class A:
    def __init__(self): print('A.__init__')

class B(A):
    def __init__(self): print('B.__init__'); super().__init__()

class C(A):
    def __init__(self): print('C.__init__'); super().__init__()

x = B()                                                # Runs B.__init__, A is next super in self's B MRO

x = C()

print('-' * 80)

class D(B, C): pass

x = D()                                                # Runs B.__init__, C is next super in self's D MRO!

print(B.__mro__)

print(D.__mro__)

print('-' * 80)

# Constraint: Call chain anchor requirement

class B:
    def __init__(self): print('B.__init__'); super().__init__()

class C:
    def __init__(self): print('C.__init__'); super().__init__()

x = B()                                                 # object is an implied super at the end of MRO

x = C()

class D(B, C): pass                                     # Inherits B.__init__ but B's MRO differs for D

x = D()                                                 # Runs B.__init__, C is next super in self's D MRO!

print(B.__mro__)

print(D.__mro__)

print('-' * 80)

class B:
    def __init__(self): print('B.__init__')

class C:
    def __init__(self): print('C.__init__')

class D(B, C):
    def __init__(self): B.__init__(self); C.__init__(self)

x = D()

# Scope: An all-or-nothing model

print('-' * 80)

class B:
    def __init__(self): print('B.__init__'); super().__init__()

class C:
    def __init__(self): print('C.__init__'); super().__init__()

class D(B, C):
    def __init__(self): print('D.__init__'); super().__init__()

X = D()

print(D.__mro__)

# What if you must use a class that doesn't call super?

class B:
    def __init__(self): print('B.__init__')

class D(B, C):
    def __init__(self): print('D.__init__'); super().__init__()

X = D()                             # It's an all-or-nothing tool...

# Flexibility: Call ordering assumptions

print('-' * 80)

# What if method call ordering needs differ from the MRO?

class B:
    def __init__(self): print('B.__init__'); super().__init__()

class C:
    def __init__(self): print('C.__init__'); super().__init__()

class D(B, C):
    def __init__(self): print('D.__init__'); C.__init__(self); B.__init__(self)

X = D()                             # It's the MRO xor explicit calls..

# Customization: Method replacement

print('-' * 80)

class A:
    def method(self): print('A.method'); super().method()

class B(A):
    def method(self): print('B.method'); super().method()

class C:
    def method(self): print('C.method')                         # No super: must anchor the chain!

class D(B, C):
    def method(self): print('D.method'); super().method()

X = D()

X.method()                                  # Dispatch to all per the MRO automatically

# What if a class needs to replace a super's default entirely?

print('-' * 40)

class B(A):
    def method(self): print('B.method')     # Drop super to replace A's method

class D(B, C):
    def method(self): print('D.method'); super().method()

X = D()

X.method()                                  # But replacement also breaks the call chain...

print('-' * 40)

class D(B, C):
    def method(self): print('D.method'); B.method(self); C.method(self)

D(). method()                               # It's back to explicit calls..

# Coupling: Application to mix-in classes

print('-' * 80)

# Mix-ins work for disjoint method sets

class A:
    def other(self): print('A.other')

class Mixin(A):
    def other(self): print('Mixin.other'); super().other()

class B:
    def method(self): print('B.method')

class C(Mixin, B):
    def method(self): print('C.method'); super().other(); super(). method()

C().method()

print(C.__mro__)

print('-' * 40)

class C(B, Mixin):
    def method(self): print('C.method'); super().other(); super().method()

C().method()

print(C.__mro__)

print('-' * 40)

# Explicit diamonds work too

class A:
    def other(self): print('A.other')

class Mixin(A):
    def other(self): print('Mixin.other'); super().other()

class B(A):
    def method(self): print('B.method')

class C(Mixin, B):
    def method(self): print('C.method'); super().other(); super().method()

C().method()

print(C.__mro__)

# Other mix-in orderings work too

print('-' * 40)

class C(B, Mixin):
    def method(self): print('C.method'); super().other(); super().method()

C().method()

print(C.__mro__)

# But direct calls work here too: explicit is better than implicit

print('-' * 40)

class C(Mixin, B):
    def method(self): print('C.method'); Mixin.other(self); B.method(self)

X = C()

X.method()

# But for nondisjoint methods: super creates overly strong coupling

print('-' * 40)

class A:
    def method(self): print('A.method')

class Mixin(A):
    def method(self): print("Mixin.method"); super().method()

Mixin().method()

class B(A):
    def method(self): print('B.method')             # super here would invoke A after B

class C(Mixin, B):
    def method(self): print('C.method'); super().method()

C().method()                                        # We miss A in this context only!

# And direct calls do not: they are immune to context of use

print('-' * 40)

class A:
    def method(self): print('A.method')

class Mixin(A):
    def method(self): print('Mixin.method'); A.method(self)

class C(Mixin, B):
    def method(self): print('C.method'); Mixin.method(self)

C().method()
