from scramble import scramble
from inter2 import intersect, union

def tester(func, items, trace = True):
    for args in scramble(items):        # Use generator (or: scramble2(items))
        if trace: print(args)
        print(sorted(func(*args)))

print(tester(intersect, ('aab', 'abcde', 'ababab')))

print(tester(intersect, ([1, 2], [2, 3, 4], [1, 6, 2, 7, 3]), False))
