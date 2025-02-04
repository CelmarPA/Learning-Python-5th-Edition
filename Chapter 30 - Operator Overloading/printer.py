class Printer:
    def __init__(self,  val):
        self.val = val

    def __str__(self):                      # Used for instance itself
        return str(self.val)                # Convert to a string result

objs = [Printer(2), Printer(3)]

for x in objs: print(x)                     # __str__ run when instance printed

print(objs)

class Printer:
    def __init__(self, val):
        self.val = val

    def __repr__(self):                     # __repr__ used by print if no __str__
        return str(self.val)                # __repr__ used if echoed or nested

objs = [Printer(2), Printer(3)]

for x in objs: print(x)                     # No __str__: runs __repr__

print(objs)                                 # Runs __repr__, not ___str__
