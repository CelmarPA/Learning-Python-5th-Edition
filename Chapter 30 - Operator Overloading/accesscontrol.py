class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10            # Not self.name=val or setattr
        else:
            raise AttributeError(attr + ' not allowed')

X = Accesscontrol()

X.age = 40                                               # Calls __setattr__

print(X.age)

X.name = 'Bob'
