def multiple(x, y):
    x = 2       # Changes local names only
    y = [3, 4]
    return x, y     # Return multiple new values in a tuple

X = 1
L = [1, 2]
X, L = multiple(X, L)       # Assign results to caller's names

print(X, L)