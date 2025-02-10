class C:
    data = 'spam'
    def __getattr__(self, name):                        # Classic in 2.X: catches built-ins
        print(name)
        return getattr(self.data, name)

X = C()
# X[0]

class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)

class C(object): pass

X = C()

X.normal = lambda: 99

print(X.normal())

X.__add__ = lambda y: 88 + y
print(X.__add__(1))

# print(X + 1)        # TypeError: unsupported operand type(s) for +: 'C' and 'int'

class C(object):
    def __getattr__(self, name):
        print(name)

X = C()

X.normal

X.__add__

# X + 1                 # TypeError: unsupported operand type(s) for +: 'C' and 'int'
