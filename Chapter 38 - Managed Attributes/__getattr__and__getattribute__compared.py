class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):                        # On undefined attrs only
        print('get: ' + attr)                           # Not on attr1: inherited from class
        if attr == 'attr3':                             # Not on attr2: stored on instance
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()

print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-' * 20)

class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()

print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-' * 20)
