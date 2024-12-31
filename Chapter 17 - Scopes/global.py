X = 88

def func():
    global X
    X = 99

func()
print(X)

y, z = 1, 2

def all_global():
    global x
    x = y + z
    return x

print(all_global())