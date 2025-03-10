class A(type): attr = 1
class B(metaclass = A): pass                    # B is meta instance and acquires meta attr

I = B()                                         # I inherits from class but not meta!

print(B.attr)

# print(I.attr)                                   # AttributeError: 'B' object has no attribute 'attr'

print('attr' in B.__dict__, 'attr' in A.__dict__)

print('-' * 80)

class A: attr = 1
class B(A): pass                                # I inherits from class and supers

I = B()

print(B.attr)

print(I.attr)

print('attr' in B.__dict__, 'attr' in A.__dict__)

print('-' * 80)

class M(type): attr = 1
class A: attr = 2
class B(A, metaclass = M): pass                     # Supers have precedence over metas

I = B()

print(B.attr, I.attr)

print('attr' in B.__dict__, 'attr' in A.__dict__, 'attr' in M.__dict__)

print('-' * 80)

class M(type): attr = 1
class A: attr = 2
class B(A): pass
class C(B, metaclass = M): pass                     # Super two levels above meta: still wins

I = C()

print(I.attr, C.attr)

print([x.__name__ for x in C.__mro__])              # See Chapter 32 for all things MRO

print(I.__class__)                                  # Followed by inheritance: instance's class

print(C.__bases__)                                  # Followed by inheritance: class's supers

print(C.__class__)                                  # Followed by instance acquisition: metaclass

print(C.__class__.attr)                             # Another way to get to metaclass attributes
