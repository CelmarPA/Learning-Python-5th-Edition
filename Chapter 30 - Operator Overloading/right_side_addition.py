class Adder:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        return self.data + other

x = Adder(5)

print(x + 2)

# print(2 + x)    # TypeError: unsupported operand type(s) for +: 'int' and 'Adder'