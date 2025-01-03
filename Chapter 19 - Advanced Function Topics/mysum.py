def mysum(l):
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])      # Call myself recursively

s = mysum([1, 2, 3, 4, 5])

print(s)

def mysum(l):
    print(l)        # Trace recursive levels
    if not l:       # L shorter at each level
        return 0
    else:
        return l[0] + mysum(l[1:])

s = mysum([1, 2, 3, 4, 5])

print(s)