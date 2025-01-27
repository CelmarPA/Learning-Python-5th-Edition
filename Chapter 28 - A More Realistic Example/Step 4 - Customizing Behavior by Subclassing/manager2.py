# Add customization of one behavior in a subclass

class Person:
    def __init__(self, name, job = 'None', pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus = .10):          # Redefine at this level
        Person.giveRaise(self, percent + bonus)         # Call Person's version

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000)        # Make a Manager: __init__
    tom.giveRaise(.10)                                             # Runs custom version
    print(tom.lastName())                                          # Runs inherited method
    print(tom)                                                     # Runs inherited __repr__
