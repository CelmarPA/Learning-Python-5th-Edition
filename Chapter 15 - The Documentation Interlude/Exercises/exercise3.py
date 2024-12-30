D = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

keys = list(D.keys())

keys.sort()

for key in keys:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])
