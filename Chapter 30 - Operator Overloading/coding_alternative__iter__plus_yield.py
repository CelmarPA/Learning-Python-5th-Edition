def gen(x):
    for i in range(x): yield i ** 2

G = gen(5)                      # Create a generator with __iter__ and __next__

print(G.__iter__() == G)        # Both methods exist on the same object

I = iter(G)                     # Runs __iter__: generator returns itself

print(next(I), next(I))         # Runs __next__ (next in 2.X)

print(list(gen(5)))             # Iteration contexts automatically run iter and next
