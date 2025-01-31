class Squares:
    def __init__(self, star, stop):             # Save state when created
        self.value = star - 1
        self.stop = stop
    def __iter__(self):                         # Get an iterator object on iter
        return self
    def __next__(self):                         # Return a square on each iteration
        if self.value == self.stop:             # Also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):               # for calls iter, which calls __iter__
    print(i, end = ' ')                         # Each iteration calls __next__

print()

X = Squares(1, 5)                     # Iterate manually: what loops do

I = iter(X)                                     # iter calls __iter__

print(next(I))                                  # next calls __next__ (in 3.X)

print(next(I))

print(next(I))

print(next(I))

print(next(I))

# print(next(I))

X = Squares(1, 5)

# print(X[1])                                     # TypeError: 'Squares' object is not subscriptable

print(list(X)[1])

X = Squares(1, 5)                       # Make an iterable with state

print([n for n in X])                             # Exhausts items: __iter__ returns self

print([n for n in X])                             # Now it's empty: __iter__ returns same self

print([n for n in Squares(1, 5)])       # Make a new iterable object

print(list(Squares(1, 3)))              # A new object for each new __iter__ call

print(36 in Squares(1, 10))             # Other iteration contexts

a, b, c = Squares(1, 3)                 # Each calls __iter__ and then __next__

print(a, b, c)

print(' : '.join(map(str, Squares(1, 5))))

X = Squares(1, 5)

print(tuple(X), tuple(X))                           # Iterator exhausted in second tuple()

X = list(Squares(1, 5))

print(tuple(X), tuple(X))
