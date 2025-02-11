from symtable import Class


class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data

I = Slotful(3)

I.a, I.b = 1, 2

print(I.a, I.b, I.c)                                    # Normal attribute fetch

print(I.__dict__)                                       # Both __dict__ and slots storage

print([x for x in dir(I) if not x.startswith('__')])

print(I.__dict__['c'])                                  # __dict__ is only one attr source

print(getattr(I, 'c'), getattr(I, 'a'))                 # dir+getattr is broader than __dict__
                                                        # applies to slots, properties, descrip

for a in (x for x in dir(I) if not x.startswith('__')):
    print(a, getattr(I, a))

class C: pass                       # Bullet 1: slots in sub but not super

class D(C): __slots__ = ['a']       # Makes instance dict for nonslots

X = D()                             # But slot name still managed in class

X.a = 1; X.b = 2

print(X.__dict__)

print(D.__dict__.keys())

class C: __slots__ = ['a']          # Bullet 2: slots in super but not sub

class D(C): pass                    # Makes instance dict for nonslots

X = D()                             # But slot name still managed in class

X.a = 1; X.b = 2

print(X.__dict__)

print(C.__dict__.keys())

class C: __slots__ = ['a']          # Bullet 3: only lowest slot accessible

class D(C): __slots__ = ['a']

class C: __slots__ = ['a']; # a = 99  # Bullet 4: no class-level defaults
# ValueError: 'a' in __slots__ conflicts with class variable

class C: __slots__ = ['a']          # Assumes universal use, differing names

class D(C): __slots__ = ['b']

X = D()

X.a = 1; X.b = 2

# print(X.__dict__)                   # AttributeError: 'D' object has no attribute '__dict__'.

print(C.__dict__.keys(), D.__dict__.keys())
