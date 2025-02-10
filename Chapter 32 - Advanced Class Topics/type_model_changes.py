class C: pass

I = C()                                 # All classes are new-style in 3.X

print(type(I), I.__class__)             # Type of instance is class it's made from

print(type(C), C.__class__)             # Class is a type, and type is a class

print(type([1, 2, 3]), [1, 2, 3].__class__)

print(type(list), list.__class__)       # Classes and built-in types work the same
