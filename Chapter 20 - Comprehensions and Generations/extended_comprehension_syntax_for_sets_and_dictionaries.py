print([x * x for x in range(10) if x % 2 == 0])         # Lists are ordered

print({x * x for x in range(10) if x % 2 == 0})         # But sets are not

print({x: x * x for x in range(10) if x % 2 == 0})      # Neither are dict keys

print([x  + y for x in [1, 2, 3] for y in [4, 5, 6]])       # Lists keep duplicates

print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})        # But sets do not

print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})         # Neither do dict keys

print({x + y for x in 'ab' for y in 'cd'})

print({x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'})

print({k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})

print({k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})