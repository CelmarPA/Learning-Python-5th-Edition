from timeit import repeat

print(min(repeat(number = 1000, repeat = 3,
                 setup = 'from mins import min1, min2, min3\n'
                         'vals = list(range(1000))',
                 stmt = 'min3(*vals)')))

print(min(repeat(number = 1000, repeat = 3,
                 setup = 'from mins import min1, min2, min3\n'
                         'import random\nvals=[random.random() for i in range(1000)]',
                stmt = 'min3(*vals)')))

import timeit

print(timeit.timeit(stmt = '[x ** 2 for x in range(1000)]', number = 1000))         # Total time

print((timeit.Timer(stmt = '[x ** 2 for x in range(1000)]').timeit(1000)))      # Class API

print(timeit.repeat(stmt = '[x ** 2 for x in range(1000)]', number = 1000, repeat = 3))

def testcase():
    y = [x ** 2 for x in range(1000)]       # Callable objects or code strings

print(min(timeit.repeat(stmt = testcase, number = 1000, repeat = 3)))
