class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):                  # __iadd__ explicit: x += y
        self.val += other                       # Usually returns self
        return self

x = Number(5)
x += 1
x += 1

print(x.val)

y = Number([1])

y += [2]
y += [3]

print(y.val)

class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):                   # __add__ fallback: x = (x + y)
        return Number(self.val + other)         # Propagates class type

x = Number(5)

x += 1
x += 1                                          # And += does concatenation here

print(x.val)
