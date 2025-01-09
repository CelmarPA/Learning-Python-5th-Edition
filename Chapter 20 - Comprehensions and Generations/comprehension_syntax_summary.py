print([x * x for x in range(10)])       # List comprehension: builds list

print((x * x for x in range(10)))       # Generator expression: produces items

print({x * x for x in range(10)})       # Set comprehension, 3.X and 2.7

print({x: x * x for x in range(10)})        # Dictionary comprehension, 3.X and 2.7
