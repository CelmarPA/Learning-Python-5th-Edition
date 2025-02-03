s = 'abcdef'
for x in s[::2]:
    for y in s[::2]:                # New objects on each iteration
        print(x + y, end = ' ')

print()

s = 'abcdef'

s = s[::2]

print(s)

for x in s:
    for y in s:                     # Same object, new iterators
        print(x + y, end = ' ')