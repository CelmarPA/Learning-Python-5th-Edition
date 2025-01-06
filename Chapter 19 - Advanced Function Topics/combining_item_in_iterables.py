from functools import reduce        # Import in 3.X, not in 2.X

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))

print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))

L = [1, 2, 3, 4]

res = L[0]

for x in L[1:]:
    res = res + x

print(res)

def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))

print(myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))

import operator, functools
print(functools.reduce(operator.add, [2, 4, 6]))       # Function-based +

print(functools.reduce((lambda x, y: x + y), [2, 4, 6]))