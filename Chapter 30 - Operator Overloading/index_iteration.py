class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


X = StepperIndex()                          # X is a StepperIndex object

X.data = "Spam"

print(X[1])                                 # Indexing calls __getitem__

for item in X:                              # for loops call __getitem__
    print(item, end = ' ')                  # for indexes items 0..N

print()

print('p' in X)                             # All call __getitem__ too

print([c for c in X])                       # List comprehension

print(list(map(str.upper, X)))              # map calls (use list() in 3.X)

(a, b, c, d) = X                            # Sequence assignments

print(a, c, d)

print(list(X), tuple(X), ''.join(X))        # And so on...

print(X)
