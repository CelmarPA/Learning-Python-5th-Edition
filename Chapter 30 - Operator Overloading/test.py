from contains import Iters

X = Iters('spam')               # Indexing

print(X[0])                     # __getitem__(0)

print('spam'[1:])               # Slice syntax

print('spam'[slice(1, None)])   # Slice object

print(X[1:])                    # __getitem__(slice(..))

print(X[:-1])

print(list(X))                  # And iteration too!
