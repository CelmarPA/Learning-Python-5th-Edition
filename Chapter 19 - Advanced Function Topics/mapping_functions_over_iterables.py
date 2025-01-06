counters = [1, 2, 3, 4]

updated = []

for x in counters:
    updated.append((x + 10))        # Add 10 to each item

print(updated)

def inc(x): return x + 10       # Function to be run

print(list(map(inc, counters)))     # Collect results

print(list(map((lambda x: x + 3), counters)))       # Function expression

def mymap(func, seq):
    res = []
    for x in seq: res.append((func(x)))
    return res

print((mymap((lambda x: x + 3),  counters)))

print(list(map(inc, [1, 2, 3])))        # Built-in is an iterable

print(mymap(inc, [1, 2, 3]))        # Ours builds a list (see generators)

print(pow(3, 4))        # 3**4

print(list(map(pow, [1, 2, 3], [2, 3, 4])))     # 1**2, 2**3, 3**4

print(list(map(inc, [1, 2, 3, 4])))

print([inc(x) for x in [1, 2, 3, 4]])       # Use () parens to generate items instead