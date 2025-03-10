# A decorator can call a metaclass, though not vice versa without type()

class MetaClass(type):
    def __new__(meta, clsname, supers, attrdict):
        print('In M.__new__:')
        print([clsname, supers, list(attrdict.keys())])
        return type.__new__(meta, clsname, supers, attrdict)

def decorator(cls):
    return MetaClass(cls.__name__, cls.__bases__, dict(cls.__dict__))

class A:
    x = 1

@decorator
class B(A):
    y = 2
    def m(self): return self.x + self.y

print(B.x, B.y)

I = B()

print(I.x, I.y, I.m())

print('-' * 80)

def Metaclass(clsname, supers, attrdict):
    return decorator(type(clsname, supers, attrdict))

def decorator(cls): ...

class B(A, metaclass = Metaclass): ...              # Metas can call decos and vice versa

def func(name, supers, attrs):
    return 'spam'

class C(metaclass = func):                          # A class whose metaclass makes it a string!
    attr = ('huh?')

print(C, C.upper())

def func(cls):
    return 'spam'

@func
class C:                                            # A class whose decorator makes it a string!
    attr  = 'huh?'

print(C, C.upper())
