print(list(range(- 5, 5)))      # An iterable in 3.X

print(list(filter((lambda x: x > 0), range(-5, 5))))        # An iterable in 3.X

res = []
for x in range(-5 , 5):     # The statement equivalent
    if x > 0:
        res.append(x)

print(res)

print([x for  x in range(-5, 5) if x > 0])      # Use () to generate items