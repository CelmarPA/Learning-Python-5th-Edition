def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2

for i in gsquares(1, 5):
    print(i, end = ' ')

print()

for i in (x ** 2 for x in range(1, 6)):
    print(i, end = ' ')

print()

print([x ** 2 for x in range(1, 6)])