def both(n):
    for i in range(n): yield i
    for i in (x ** 2 for x in range(n)): yield i

print(list(both(5)))

def both(n):
    yield from range(n)
    yield from (x ** 2 for x in range(n))

print(list(both(5)))

print(' : '.join(str(i) for i in both(5)))
