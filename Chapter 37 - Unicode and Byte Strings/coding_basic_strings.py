B = b'spam'
S = 'eggs'

print(type(B), type(S))

print(B)

print(S)

print(B[0], S[0])               # Indexing returns an int for bytes, str for str

print(B[1:], S[1:])             # Slicing makes other bytes or str object

print(list(B), list(S))         # bytes is really 8-bit small ints

# B[0] = 'x'                      # TypeError: 'bytes' object does not support item assignment

# S[0] = 'x'                      # TypeError: 'str' object does not support item assignment

# bytes prefix works on single, double, triple quotes, raw

B = B"""
xxxx
yyyy
"""

print(B)

U = u'spam'

print(type(U))

print(U)

print(U[0])

print(list(U))
