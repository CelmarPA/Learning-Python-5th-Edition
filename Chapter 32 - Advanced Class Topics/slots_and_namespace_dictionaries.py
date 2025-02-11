class C:
    __slots__ = ['a', 'b']                      # __slots__ means no __dict__ by default

X = C()

X.a = 1

print(X.a)

# print(X.__dict__)               # AttributeError: 'C' object has no attribute '__dict__'

print(getattr(X, 'a'))

setattr(X, 'b', 2)                # But getattr() and setattr() still work

print(X.b)

print('a' in dir(X))              # And dir() finds slot attributes too

print('b' in dir(X))

class D:                          # Use D(object) for same result in 2.X
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 4                # Cannot add new names if no __dict__

# X = D()                           # AttributeError: 'D' object has no attribute 'd'

class D:
    __slots__ = ['a', 'b', '__dict__']          # Name __dict__ to include one too
    c = 3
    def __init__(self):
        self.d = 4                              # d stored in __dict__, a is a slot

X = D()

print(X.d)

print(X.c)

# All instance attrs undefined until assigned
# print(X.a)                        # AttributeError: 'D' object has no attribute 'a'

X.a = 1
X.b = 2

print(X.__dict__)                   # Some objects have both __dict__ and slot names
                                    # getattr() can fetch either type of attr
print(X.__slots__)

print(getattr(X, 'a'), getattr(X, 'c'), getattr(X, 'd'))

for attr in list(X.__dict__) + X.__slots__:  # Wrong
    print(attr, '=>', getattr(X, attr))

# Less wrong...
for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))
