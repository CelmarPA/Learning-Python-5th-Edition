from urllib.response import addbase


class Adder:
    def __init__(self, value = 0):
        self.data = value                   # Initialize data

    def __add__(self, other):
        self.data += other                  # Add other in place (bad form?)


x = Adder()                                 # Default displays

print(x)

class Addrepr(Adder):                       # Inherit __init__, __add__
    def __repr__(self):                     # Add string representation
        return 'Addrepr(%s)' % self.data    # Convert to as-code string

x = Addrepr(2)                              # Runs __init__

x + 1                                       # Runs __add__ (x.add() better?)

print(x)                                    # Runs __repr__

print(str(x), repr(x))                      # Runs __repr__ for both

class Addstr(Adder):
    def __str__(self):                      # __str__ but no __repr__
        return '[Value: %s]' % self.data    # Convert to nice string

x = Addstr(3)

x + 1

print(x)                                    # Runs __str__

print(str(x), repr(x))

class Addboth(Adder):
    def __str__(self):
        return '[Value: %s]' % self.data            # User-friendly string

    def __repr__(self):
        return 'Addboth(%s)' % self.data            # As-code string

x = Addboth(4)

x + 1

print(x)                                            # Runs __str__

print(str(x), repr(x))
