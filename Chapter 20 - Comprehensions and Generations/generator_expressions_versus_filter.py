line = 'aa bbb c'

print(''.join(x for x in line.split() if len(x) > 1))       # Generator with 'if'

print(''.join(filter(lambda x: len(x) > 1, line.split())))      # Similar to filter

print(''.join(x.upper() for x in line.split() if len(x) > 1))

print(''.join(map(str.upper, filter(lambda x: len(x) > 1,  line.split()))))

print(''.join(x.upper() for x in line.split() if len(x) > 1))

res = ''
for x in line.split():      # Statement equivalent?
    if len(x) > 1:      # This is also a join
        res += x.upper()

print(res)
