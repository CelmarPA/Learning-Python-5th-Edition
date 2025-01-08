L, S = [1, 2, 3], 'spam'

for i in range(len(S)):         # For repeat counts 0..3
    S = S[1:] + S[:1]       # Move front item to the end
    print(S, end = ' ')

print('\n')

for i in range(len(L)):
    L = L[1:] + L[:1]       # Slice so any sequence type works
    print(L, end = ' ')

print('\n')

for i in range(len(S)):         # For positions 0..3
    X = S[i:] + S[:i]       # Rear part + front part (same effect)
    print(X, end = ' ')
