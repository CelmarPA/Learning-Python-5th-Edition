class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, '+', other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, '+', other)
        return other + self.val

class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('radd', self.val, '+', other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)                  # Call __add__ explicitly

class Commuter3:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('radd', self.val, '+', other)
        return self.val + other

    def __radd__(self, other):
        return self + other                         # Swap order and re-add

class Commuter4:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('radd', self.val, '+', other)
        return self.val + other
    __radd__ = __add__                              # Alias: cut out the middleman


class Commuter5:                                    # Propagate class type in results
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):            # Type test to avoid object nesting
            other = other.val
        return Commuter5(self.val + other)          # Else + result is another Commuter

    def __radd__(self, other):
        return Commuter5(other + self.val)

    def __str__(self):
        return '<Commuter5: %s>' % self.val
