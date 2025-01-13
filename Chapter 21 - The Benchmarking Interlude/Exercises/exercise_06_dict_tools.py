def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new

d = {1: 1, 2: 2}

e = copyDict(d)

d[2] = '?'

print(d)

print(e)

# The X[:] doesn't work for dictionaries, as they're not sequences.
