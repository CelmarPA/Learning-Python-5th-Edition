G = (c * 4 for c in 'SPAM')

print(iter(G) is G)         # My iterator is myself: G has __next__

G = (c * 4 for c in 'SPAM')         # Make a new generator

I1 = iter(G)        # Iterate manually

print(next(I1))
print(next(I1))

I2 = iter(G)        # Second iterator at same position!

print(next(I2))

print(list(I1))         # Collect the rest of I1's items

# print(next(I2))         # Other iterators exhausted too "StopIteration"

I3 = iter(G)        # Ditto for new iterators

I3 = iter(c * 4 for c in 'SPAM')        # New generator to start over

print(next(I3))

def timesfour(s):
    for c in s:
        yield c * 4

G = timesfour('spam')       # Generator functions work the same way

print(iter(G) is G)

I1, I2 = iter(G), iter(G)

print(next(I1))
print(next(I1))
print(next(I2))         # I2 at same position as I1

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

print(next(I1))
print(next(I1))
print(next(I2))         # Lists support multiple iterators

del(L[2:])      # Changes reflected in iterators
print(next(I1))         # "StopIteration"
