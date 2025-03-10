class C:                                        # Inheritance special case #2...
    attr = 1                                    # Inheritance special case #2...
    def __str__(self): return('class')

I = C()

print(I.__str__(), str(I))                      # Both from class if not in instance

I.__str__ = lambda: 'instance'

print(I.__str__(), str(I))                      # Explicit=>instance, built-in=>class!

print(I.attr)                                   # Asymmetric with normal or explicit names

I.attr = 2

print(I.attr)

print('-' * 80)

class D(type):
    def __str__(self): return('D class')

class C(D):
    pass

print(C.__str__(C), str(C))                     # Explicit=>super, built-in=>metaclass!

class C(D):
    def __str__(self): return('C class')

print(C.__str__(C), str(C))                     # Explicit=>class, built-in=>metaclass!

class C(metaclass = D):
    def __str__(self): return('C class')

print(C.__str__(C), str(C))                     # Built-in=>user-defined metaclass

print('-' * 80)

class C(metaclass = D):
    pass

print(C.__str__(C), str(C))                     # Explicit=>object, built-in=>metaclass

print(C.__str__)

for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])
