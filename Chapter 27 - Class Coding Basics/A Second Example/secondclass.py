class FirstClass:                   # Define a class object
    def setData(self, value):       # Define class methods
        self.data = value           # self is the instance
    def display(self):
        print(self.data)            # self.data: per instance

class SecondClass(FirstClass):          # Inherits setData
    def display(self):                  # Changes display
        print('Current value = "%s"' % self.data)

z = SecondClass()

z.setData(42)       # Finds setData in FirstClass

z.display()         # Finds overridden method in SecondClass
