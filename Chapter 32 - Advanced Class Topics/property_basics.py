class Operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

x = Operators()

print(x.age)                                    # Runs __getattr__

# print(x.name)                                   # Runs __getattr__
# AttributeError: name

class Properties(object):                       # Need object in 2.X for setters
    def getage(self):
        return 40
    age = property(getage, None, None, None)    # (get, set, del, docs), or use @

x = Properties()

print(x.age)                                    # Runs getage

# print(x.name)                                 # AttributeError: 'properties' object has no attribute 'name'

class Properties(object):
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)

x = Properties()

print(x.age)                                     # Runs getage

x.age = 42

print(x._age)                                    # Normal fetch: no getage call

print(x.age)                                     # Runs getage

x.job = 'trainer'                                # Normal assign: no setage call

print(x.job)

class Operators:
    def __getattr__(self, name):                 # On undefined reference
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):          # On all assignments
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value        # Or object.__setattr__()
        else:
            self.__dict__[name] = value

x = Operators()

print(x.age)                                     # Runs __getattr__

x.age = 41                                       # Runs __setattr__

print(x._age)                                    # Defined: no __getattr__ call

print(x.age)                                     # Runs __getattr__

x.job = 'trainer'                                # Runs __setattr__ again

print(x.job)                                     # Defined: no __getattr__ call
