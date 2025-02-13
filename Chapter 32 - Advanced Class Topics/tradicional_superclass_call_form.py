class C:
    def act(self):
        print('spam')

class D(C):
    def act(self):
        C.act(self)                 # Name superclass explicitly, pass self
        print('eggs')

X = D()

X.act()

# Basic super Usage and Its Tradeoffs

class C:                            # In Python 3.X (only: see 2.X super form ahead)
    def act(self):
        print('spam')

class D(C):
    def act(self):
        super().act()               # Reference superclass generically, omit self
        print('eggs')

X = D()

X.act()

print(super)                        # A "magic" proxy object that routes later calls

# print(super())                    # SystemError: super(): no arguments

class E(C):
    def method(self):               # self is implicit in super...only!
        proxy = super()             # This form has no meaning outside a method
        print(proxy)                # Show the normally hidden proxy object
        proxy.act()                 # No arguments: implicitly calls superclass method!

E().method()

# Pitfall: Adding multiple inheritance naively

class A:
    def act(self): print('A')

class B:
    def act(self): print('B')
    
class C(A):
    def act(self):
        super().act()               # super applied to a single-inheritance tree

X = C()

X.act()

class C(A, B):                      # Add a B mix-in class with the same method
    def act(self):
        super().act()               # Doesn't fail on multi-inher, but picks just one!

X = C()

X.act()

class C(B, A):
    def act(self):
        super().act()               # If B is listed first, A.act() is no longer run!

X = C()

X.act()

class C(A, B):                      # Traditional form
    def act(self):                  # You probably need to be more explicit here
        A.act(self)                 # This form handles both single and multiple inher
        B.act(self)                 # And works the same in both Python 3.X and 2.X

X = C()

X.act()

# Limitation: Operator overloading

class C:                            # In Python 3.X
    def __getitem__(self, ix):      # Indexing overload method
        print('C index')

class D(C):
    def __getitem__(self, ix):      # Redefine to extend here
        print('D index')
        C.__getitem__(self, ix)     # Traditional call form works
        super().__getitem__(ix)     # Direct name calls work too
        super()[íx]                 # But operators do not! (__getattribute__)

X = C()

X[99]

X = D()

X[99]
"""
Traceback (most recent call last):
File "", line 1, in
File "", line 6, in __getitem__
TypeError: 'super' object is not subscriptable
This behavior is due to the very same new-style (and
"""
