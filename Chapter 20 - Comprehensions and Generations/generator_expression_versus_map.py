print(list(map(abs, (-1, -2, 3 ,4))))       # Map function on tuple

print(list(abs(x) for x in (-1, -2, 3, 4)))         # Generator expression

print(list(map(lambda x: x * 2, (1, 2, 3, 4))))         # Nonfunction case

print(list(x * 2 for x in (1, 2, 3, 4)))        # Simpler as generator?

line = 'aaa,bbb,ccc'

print(''.join([x.upper() for x in line.split(',')]))        # Makes a pointless list

print(''.join(x.upper() for x in line.split(',')))      # Generates results

print(''.join(map(str.upper,  line.split(','))))        # Generates results

print(''.join(x * 2 for x in line.split(',')))      # Simpler as generator?

print(''.join(map(lambda x: x * 2, line.split(','))))

print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])        # Nested comprehensions

print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))     # Nested maps

print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))        # Nested generators

import math

print(list(map(math.sqrt, (x ** 2 for x in range(4)))))     # Nested combinations

print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))       # Nesting gone bad?

print(list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1)))))

print(list(abs(x) * 2 for x in (-1, 2, 3, 4)))      # Unnested equivalents

print(list(math.sqrt(x ** 2) for x in range(4)))        # Flat is often better

print(list(abs(x) for x in (-1, 0, 1)))
