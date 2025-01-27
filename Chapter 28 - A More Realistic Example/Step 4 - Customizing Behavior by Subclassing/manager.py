from person import Person

# Define a subclass of Person
class Manager(Person):                                  # Inherit Person attrs
    # Augmenting Methods: The Bad Way
    def giveRaise(self, percent, bonus = .10):          # Redefine to customize
        self.pay = int(self.pay * (1 + percent + bonus))

class Manager(Person):
    # Augmenting Methods: The Good Way
    def giveRaise(self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)         # Good: augment original

