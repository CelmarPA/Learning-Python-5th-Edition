from idlelib.squeezer import Squeezer


class Squares:
    def __init__(self, start, stop):                # Non-yield generator
        self.start = start                          # Multiscans: extra object
        self.stop = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):
    print(i,  end = ' ')

print()

S = Squares(1, 5)

I = iter(S)

print(next(I), next(I))

J = iter(S)                                 # Multiple iterators without yield
print(next(J))

print(next(I))

S = Squares(1, 3)
for i in S:                                 # Each for calls __iter___
    for j in S:
        print('%s:%s' % (i, j), end=' ')