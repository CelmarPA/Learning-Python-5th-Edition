print([x ** 2 for x in range(4)])       # List comprehension: build a list

print((x ** 2 for x in range(4)))       # Generator expression: make an iterable

print(list((x ** 2 for x in range (4))))        # List comprehension equivalence

G = (x ** 2 for x in range(4))

print(iter(G) is G)         # iter(G) optional: __iter__ returns self

print(next(G))
print(next(G))
print(next(G))
print(next(G))
# print(next(G))

print(G)

for num in (x ** 2 for x in range(4)):      # Calls next() automatically
    print(f'{num}, {num / 2.0}')
    # print('%s, %s' % (num, num / 2.0))

print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, b, c)

print(sum(x ** 2 for x in range(4)))        # Parens optional

print(sorted(x ** 2 for x  in range(4)))        # Parens optional

print(sorted((x ** 2 for x in range(4)), reverse = True))       # Parens required
