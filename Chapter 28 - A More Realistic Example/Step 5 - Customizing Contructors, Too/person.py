# Add customization of constructor in a subclass

class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' %(self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):                          # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)         # Run original with 'mgr'

    def giveRaise(self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)              # Job name isn't needed:
    tom.giveRaise(.10)                                        # Implied/set by class
    print(tom.lastName())
    print(tom)
