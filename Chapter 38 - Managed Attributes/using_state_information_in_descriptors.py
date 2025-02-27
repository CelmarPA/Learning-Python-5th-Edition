from typing import overload


class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):                 # On attr fetch
        print('DescState get')
        return self.value * 10

    def __set__(self, instance, value):                 # On attr assign
        print('DescState set')
        self.value = value

# Client Class

class CalcAttrs:
    X = DescState(2)                                    # Descriptor class attr

    Y = 3                                               # Class attr

    def __init__(self):                                 # Instance attr
        self.Z = 4

obj = CalcAttrs()

print(obj.X, obj.Y, obj.Z)                              # X is computed, others are not

obj.X = 5                                               # X assignment is intercepted

CalcAttrs.Y = 6                                         # Y reassigned in class

obj.Z = 7                                               # Z assigned in instance

print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()

print(obj2.X, obj2.Y, obj2.Z)                           # But X uses shared data, like Y!

print('-' * 80)

class InstState:
    def __get__(self, instance, owner):
        print('Instance get')                           # Assume set by client class
        return instance._X * 10

    def __set__(self, instance, value):
        print('Instance set')
        instance._X = value

# Cliente Class

class CalcAttrs:
    X =  InstState()                                     # Descriptor class attr
    Y = 3                                                # Class attr
    def __init__(self):
        self.X = 2                                       # Instance attr
        self.Z = 4                                       # Instance attr

obj = CalcAttrs()

print(obj.X, obj.Y, obj.Z)                               # X is computed, others are not

obj.X = 5                                                # X assignment is intercepted

CalcAttrs.Y = 6                                          # Y reassigned in class

obj.Z = 7                                                # Z assigned in instance

print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                                        # But X differs now, like Z!

print(obj2.X, obj2.Y, obj2.Z)

print('-' * 80)

class DescBoth:
    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)

    def __set__(self, instance, value):
        instance.data = value

class Client:
    def __init__(self, data):
        self.data = data

    managed = DescBoth('spam')

I = Client('eggs')

print(I.managed)                                            # Show both data sources

I.managed = 'SPAM'                                          # Change instance data

print(I.managed)

print(I.__dict__)

print([x for x in dir(I) if not x.startswith('__')])

print(getattr(I, 'data'))

print(getattr(I, 'managed'))

for attr in (x for x in dir(I) if not x.startswith('__')):
    print('%s => %s' % (attr, getattr(I, attr)))
