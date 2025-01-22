class FirstClass:                   # Define a class object
    def setData(self, value):       # Define class methods
        self.data = value           # self is the instance
    def display(self):
        print(self.data)            # self.data: per instance

x = FirstClass()        # Make two instances

y = FirstClass()        # Each is a new namespace


x.setData("King Arthur")            # Call methods: self is x

y.setData(3.14159)                  # Runs: FirstClass.setData(y, 3.14159

x.display()             # self.data differs in each instance

y.display()             # Runs: FirstClass.display(y)

x.data = "New value"                # Can get/set attributes

x.display()                         # Outside the class too

x.anotherName = "spam"              # Can set new attributes here too!