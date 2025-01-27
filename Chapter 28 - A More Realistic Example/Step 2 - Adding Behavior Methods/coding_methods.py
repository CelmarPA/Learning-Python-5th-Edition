# Add methods to encapsulate operations for maintainability

class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):                     # Behavior methods
        return self.name.split()[-1]        # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))        # Must change here only

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())               # Use the new methods
    sue.giveRaise(.10)                                  # instead of hardcoding
    print(sue.pay)
