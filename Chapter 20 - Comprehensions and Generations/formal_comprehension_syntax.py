# [ expression for target in iterable ]

"""
    [ expression for target1 in iterable1 if condition1
                for target2 in iterable2 if condition2 ...
                for targetN in iterableN if conditionN ]

"""

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print(res)

print([x + y for x in 'spam' for y in 'SPAM'])

print([x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')])

print([x + y + z for x in 'spam' if x in 'sm'
                 for y in 'SPAM' if y in ('P', 'A')
                 for z in '123'  if z > '1'])

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))

print(res)