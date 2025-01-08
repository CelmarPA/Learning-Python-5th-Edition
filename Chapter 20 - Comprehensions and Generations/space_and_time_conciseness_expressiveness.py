import math

print(math.factorial(10))       # 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

from permute import permute1, permute2

seq = list(range(10))

p1 = permute1(seq)      # Creates a list of 3.6M numbers

print(len(p1), p1[0],  p1[1])

p2 = permute2(seq)      # Returns generator immediately

print(next(p2))         # And produces each result quickly on request

print(next(p2))

p2 = list(permute2(seq))        # About 28 seconds, though still impractical

print(p1 == p2)         # Same set of results generated

print(math.factorial(50))

p3 = permute2(list(range(50)))

print(next(p3))         # permute1 is not an option here!

import random

print(math.factorial(20))       # permute1 is not an option here

seq = list(range(20))

random.shuffle(seq)         # Shuffle sequence randomly first

p = permute2(seq)

print(next(p))

print(next(p))

random.shuffle(seq)

p = permute2(seq)

print(next(p))

print(next(p))
