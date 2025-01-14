import math
from functools import reduce
from timeit import repeat
from math import factorial

def fact0(n):       # Recursive
    if n == 1:      # Fails at 999 by default
        return n
    else:
        return n * factorial(n - 1)

def fact1(n):       # Recursive, one-liner
    return n if n == 1 else n * fact1(n - 1)

def fact2(n):       # Functional
    return reduce(lambda x, y: x * y, range(1, n + 1))

def fact3(n):
    res = 1
    for i in range(1, n + 1): res *= i      # Iterative
    return res

def fact4(n):
    return math.factorial(n)        # Stdlib "batteries"

# Tests

print(fact0(6), fact1(6), fact2(6), fact3(6), fact4(6))

print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500))

for test in (fact0, fact1, fact2, fact3, fact4):
    print(test.__name__, min(repeat(stmt = lambda: test(500), number = 20, repeat = 3)))

def rev1(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + rev1(s[:-1])         # Recursive: 10x slower in CPython today

def rev2(s):
    return ''.join(reversed(s))         # Non-recursive iterable: simpler, faster

def rev3(s):
    return s[::-1]      # Even better?: sequence reversal by slice



for test in (rev1, rev2, rev3):
    print(test.__name__, min(repeat(stmt = lambda: test('spam, ham, eggs'), number = 20, repeat = 3)))
