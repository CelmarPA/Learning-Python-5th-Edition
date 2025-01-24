class FirstClass:                   # Define a class object
    def setData(self, value):       # Define class methods
        self.data = value           # self is the instance
    def display(self):
        print(self.data)            # self.data: per instance

class SecondClass(FirstClass):          # Inherits setData
    def display(self):                  # Changes display
        print('Current value = "%s"' % self.data)

class ThirdClass(SecondClass):          # Inherit from SecondClass
    def __init__(self, value):          # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other):           # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):               # On "self + other"
        self.data *= other

a = ThirdClass('abc')           # __init__ called

a.display()                     # Inherited method called

print(a)                        # __str__: returns display string

b = a + 'xyz'                   # __add__: makes a new instance

b.display()                     # b has all ThirdClass methods

print(b)                        # __str__: returns display string

a.mul(3)                        # mul: changes instance in place

print(a)
