S1 = 'abc'

S2 = 'xyz123'

print(list(zip(S1, S2)))        # zip pairs items from iterables

# zip pairs items, truncates at shortest
print(list(zip([-2, -1, 0, 1, 2])))         # Single sequence: 1-ary tuples

print(list(zip([1, 2, 3], [2, 3, 4, 5])))       # N sequences: N-ary tuples

# map passes paired items to functions, truncates
print(list(map(abs, [-2, -1 ,0, 1, 2])))        # Single sequence: 1-ary function

print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))

# map and zip accept arbitrary iterables
print(list(map(lambda x, y: x + y, open('script2.py'), open('script2.py'))))

print([x + y for (x, y) in zip(open('script2.py'), open('script2.py'))])