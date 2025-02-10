class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)

X = C()

print(X.__getitem__(1))                 # Traditional mapping works but new-style's does not

# print(X[1])                           # TypeError: 'C' object does not support indexing

# print(type(X).__getitem__(X, 1))      # AttributeError: type object 'C' has no attribute '__getitem__'.

print(X.__add__('eggs'))                # Ditto for +: instance skipped for expression only

# print(X + 'eggs')                     # TypeError: unsupported operand type(s) for +: 'C' and 'str'

# print(type(X).__add__(X, 'eggs'))     # AttributeError: type object 'C' has no attribute '__add__'.

class C(object):                        # New-style: 3.X and 2.X
    data = 'spam'
    def __getattr__(self, name):        # Catch normal names
        print('getattr: ' + name)
        return getattr(self.data, name)
    def __getitem__(self, i):
        print('getitem: ' + str(i))
        return self.data[i]
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)

X = C()

print(X.upper)

print(X.upper())

print(X[1])                                 # Built-in operation (implicit)

print(type(X).__getitem__(X, 1))         # New-style equivalence

print(X + 'eggs')                           # Ditto for + and others

print(X.__add__('eggs'))

print(type(X).__add__(X, 'eggs'))
