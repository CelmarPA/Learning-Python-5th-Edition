#  a:

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(X, 'not found')

#  b:

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for p in L:
    if (2 ** X) == p:
        print((2 ** X),  'was found at', L.index(p))
        break
else:
    print(X, 'not found')

# c:

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if (2 ** X) in L:
    print((2 ** X),  'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# d:

X = 5
L = []

for i in range(7):
    L.append(2 ** i)

print(L)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'was not found')

# e:

target = 2 ** X

if target in L:
    print(target, 'was found at', L.index(target))
else:
    print(X, 'was not found')

# f:

X = 5

L = list(map(lambda x: 2 ** x, range(7)))

print(L)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'was not found')
