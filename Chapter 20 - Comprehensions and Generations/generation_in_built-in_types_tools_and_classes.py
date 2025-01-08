D = {'a': 1, 'b': 2, 'c': 3}

x = iter(D)

print(next(x))
print(next(x))

for key in D:
    print(key, ' => ', D[key])

for line in open('temp.txt'):
    print(line, end = '')
