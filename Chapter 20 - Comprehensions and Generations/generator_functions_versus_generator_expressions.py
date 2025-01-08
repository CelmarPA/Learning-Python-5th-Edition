G = (c * 4 for c in 'SPAM')         # Generator expression
print(list(G))          # Force generator to produce all results

def timesfour(s):           # Generator function
    for c in s:
        yield c * 4

G = timesfour('spam')
print(list(G))          # Iterate automatically

G = (c * 4 for c in 'SPAM')
I = iter(G)         # Iterate manually (expression)
print(next(I))
print(next(I))


G = timesfour('spam')
I = iter(G)         # Iterate manually (function)
print(next(I))
print(next(I))

line = 'aa bbb c'

print(''.join(x.upper() for x in line.split() if len(x) > 1))           # Expression

def gensub(line):           # Function
    for x in line.split():
        if len(x) > 1:
            yield x.upper()

print(''.join(gensub(line)))            # But why generate?
