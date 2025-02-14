from typing import Literal


class Adder:
    def add(self, x, y):
        print('Not Implemented!')

    def __init__(self, start = []):
        self.data = start

    def __add__(self, other):
        return self.add(self.data, other)

class ListAdder(Adder):
    def add(self, x, y):
        print(x + y)
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        new = {}
        for k in x.keys(): new[k] = x[k]
        for k in y.keys(): new[k] = y[k]
        print(new)
        return new

x = Adder()

x.add(1, 2)

x = ListAdder()

x.add([1], [2])

x = DictAdder()

x.add({1:1}, {2:2})

x = Adder([1])

x + [2]

x = ListAdder([1])

x + [2]

class Adder:
    def __init__(self, start = []):
        self.data = start

    def __add__(self, other):
        return self.add(other)

    def add(self, y):
        print('Not implemented!')

class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        d = self.data.copy()
        d.update(y)
        return d

x = ListAdder([1, 2, 3])

y = x + [4 , 5, 6]

print(y)

z = DictAdder(dict(name = 'bob')) + {'a': 1}

print(z)