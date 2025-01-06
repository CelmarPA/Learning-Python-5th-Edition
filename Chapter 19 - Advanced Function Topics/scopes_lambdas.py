def action(x):
    return (lambda  y: x + y)       # Make and return function, remember x

act = action(99)

print(act)

print(act(2))       # Call what action returned

action = (lambda x: (lambda y: x + y))

act = action(99)

print(act(3))

print((lambda x: (lambda y: x + y))(99)(4))