from modclass import FirstClass             # Copy name into my scope

class SecondClass(FirstClass):              # Use class name directly
    def display(self):
        print('Current value = "%s"' % self.data)