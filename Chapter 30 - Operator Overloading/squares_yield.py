class Squares:                               # __iter__ + yield generator
    def __init__(self, start, stop):         # __next__ is automatic/implied
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

for i in Squares(1, 5):
    print(i, end = ' ')

print()

S = Squares(1, 5)                   # Runs __init__: class saves instance state

print(S)

I = iter(S)                                    # Runs __iter__: returns a generator

"""print(I)

print(next(I))

print(next(I))                                  # Runs generator's __next__

print(next(I))

print(next(I))

print(next(I))

print(next(I))"""