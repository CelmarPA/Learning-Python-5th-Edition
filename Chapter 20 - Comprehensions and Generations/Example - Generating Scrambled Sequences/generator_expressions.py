S =  'spam'

G = (S[i:] + S[:i] for i in range(len(S)))      # Generator expression equivalent

print(list(G))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

print(F(S))

print(list(F(S)))

print(list(F([1, 2, 3])))

for x in F((1, 2, 3)):
    print(x, end = ' ')
