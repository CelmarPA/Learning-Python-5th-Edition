def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

f(0, 1, 2)      # Normal positionals

f(*range(3))        # Unpack range values: iterable in 3.X

f(*(i for i in range(3)))       # Unpack generator expression values

D = dict(a = 'Bob', b = 'dev', c = 40.5)

print(D)

f(a = 'Bob', b = 'dev', c = 40.5)       # Normal keywords

f(**D)      # Unpack dict: key=value

f(*D)       # Unpack keys iterator

f(*D.values())      # Unpack view iterator: iterable in 3.X

for x in 'spam': print(x.upper(), end = ' ');

print('\n')

print(list(print(x.upper(), end = ' ') for x in 'spam'))

print(*(x.upper() for x in 'spam'))