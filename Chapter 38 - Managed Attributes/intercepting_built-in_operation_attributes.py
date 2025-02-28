class GetAttr:
    eggs = 88                   # eggs stored on class, spam on instance
    def __init__(self):
        self.spam = 77

    def __len__(self):          # len here, else __getattr__ called with __len__
        print('__len__: 42')
        return 42

    def __getattr__(self, attr):        # Provide __str__ if asked, else dummy func
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute:
    eggs = 88
    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))

    X = Class()
    X.eggs                  # Class attr
    X.spam                  # Instance attr
    X.other                 # Missing attr
    len(X)                  # __len__ defined explicitly

# New-styles must support [], +, call directly: redefine
    try:    X[0]                # __getitem__?
    except: print('fail []')

    try:    X + 99              # __add__?
    except: print('fail +')

    try:    X()                 # __call__? (implicit via built-in)
    except: print('fail ()')

    X.__call__()                # __call__? (explicit, not inherited
    print(X.__str__())          # __str__? (explicit, inherited from type)
    print(X)

print('-' * 80)

# Delegation-based managers revisited

class Person:
    def __init__(self, name, job = None,  pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)              # Embed a Person object

    def giveRaise(self, percent, bonus = .10):
        self.person.giveRaise(percent + bonus)                  # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)                       # Delegate all other attrs

    def __repr__(self):
        return str(self.person)                                 # Must overload again (in 3.X)

if __name__ == '__main__':
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)                # Manager.__init__
    print(tom.lastName())                                       # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                                          # Manager.giveRaise -> Person.giveRaise
    print(tom)                                                  # Manager.__repr__ -> Person.__repr__

print('-' * 80)

# Delete the Manager __str__ method

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)              # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)                  # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)                       # Delegate all other attrs

if __name__ == '__main__':
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)                # Manager.__init__
    print(tom.lastName())                                       # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                                          # Manager.giveRaise -> Person.giveRaise
    print(tom)                                                  # Manager.__repr__ -> Person.__repr__

print('-' * 80)

# Replace __getattr_ with __getattribute__

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name,  'mgr', pay)             # Embed a Person object

    def giveRaise(self, percent, bonus = .10):
        self.person.giveRaise(percent + bonus)                  # Intercept and delegate

    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)          # Fetch my attrs
        else:
            return getattr(self.person, attr)                   # Delegate all others

if __name__ == '__main__':
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)                # Manager.__init__
    print(tom.lastName())                                       # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                                          # Manager.giveRaise -> Person.giveRaise
    print(tom)                                                  # Manager.__repr__ -> Person.__repr__

print('-' * 80)

# Code __getattribute__ differently to minimize extra calls

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def __getattribute__(self, attr):
        print('**', attr)
        person = object.__getattribute__(self, 'person')
        if attr == 'giveRaise':
            return lambda percent: person.giveRaise(percent + .10)
        else:
            return getattr(person, attr)

    def __repr__(self):
        person = object.__getattribute__(self, 'person')
        return str(person)

if __name__ == '__main__':
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)                # Manager.__init__
    print(tom.lastName())                                       # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                                          # Manager.giveRaise -> Person.giveRaise
    print(tom)                                                  # Manager.__repr__ -> Person.__repr__

print('-' * 80)
