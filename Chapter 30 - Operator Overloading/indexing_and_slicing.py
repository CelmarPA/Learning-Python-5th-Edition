class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()

print(X[2])                         # X[i] calls X.__getitem__(i)

for i in range(5):
    print(X[i], end= ' ')           # Runs __getitem__(X, i) each time

print()

# Intercepting Slices

L = [5, 6, 7, 8, 9]

print(L[2:4])                       # Slice with slice syntax: 2..(4-1)
print(L[1:])
print(L[:-1])
print(L[::2])

print(L[slice(2, 4)])
print(L[slice(1, None)])
print(L[slice(None, -1)])
print(L[slice(None, None, 2)])

class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):           # Called for index or slice
        print('getitem:',  index)
        return self.data[index]             # Perform index or slice

X = Indexer()

print(X[0])                                 # Indexing sends __getitem__ an integer

print(X[1])

print(X[-1])

print(X[2:4])                               # Slicing sends __getitem__ a slice object

print(X[1:])

print(X[:-1])

print(X[::2])

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

X = Indexer()

print(X[99])

print(X[1:99:2])

print(X[1:])

class IndexSetter:
    def __setitem__(self, index, value):                # Intercept index or slice assignment
        ...
        self.data[index] = value                        # Assign index or slice


class C:
    def __index__(self):
        return 255

X = C()

print(hex(X))                                           # Integer value

print(bin(X))

print(oct(X))

print(('C' * 256)[255])

print(('C' * 256)[X])                                   # As index (not X[i])

print(('C' * 256)[X:])                                  # As index (not X[i:])