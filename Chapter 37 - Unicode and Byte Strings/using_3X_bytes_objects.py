# Method Calls

# Attributes in str but not bytes
print(set(dir('abc')) - set(dir(b'abc')))

# Attributes in bytes but not str
print(set(dir(b'abc')) - set(dir('abc')))

B = b'spam'                                 # b'...' bytes literal]

print(B.find(b'pa'))

print(B.replace(b'pa', b'XY'))  # bytes methods expect bytes arguments

print(B.split(b'pa'))                       # bytes methods return bytes results

print(B)

# B[0] = 'x'                                  # TypeError: 'bytes' object does not support item assignment

print('%s' % 99)

# print(b'%s' % 99)                           # TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'int'

print('{0}'.format(99))

# print(b'{0}'.format(99))                    # AttributeError: 'bytes' object has no attribute 'format'

print('-' * 80)

# Sequence Operations

B = b'spam'                                 # A sequence of small ints

print(B)                                    # Prints as ASCII characters (and/or hex escapes)

print(B[0])                                 # Indexing yields an int

print(B[-1])

print(chr(B[0]))                            # Show character for int

print(list(B))                              # Show all the byte's int values

print(B[1:], B[:-1])

print(len(B))

print(B + b'lmn')

print(B * 4)

print('-' * 80)

# Other Ways to Make bytes Objects

B = b'abc'                                 # Literal

print(B)

B = bytes('abc', 'ascii')                   # Constructor with encoding name

print(B)

print(ord('a'))

B = bytes([97, 98, 99])                     # Integer iterable

print(B)

B = 'spam'.encode()                         # str.encode() (or bytes())

print(B)

S = B.decode()                              # bytes.decode() (or str())

print(S)

print('-' * 80)

# Mixing String Types

# Must pass expected types to function and method calls

B = b'spam'

# B.replace('pa', 'XY')                     # TypeError: a bytes-like object is required, not 'str'

print(B.replace(b'pa', b'XY'))

B = B'spam'

# B.replace(bytes('pa'), bytes('xy'))         # TypeError: string argument without an encoding

print(B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8')))

# Must convert manually in 3.X mixed-type expressions

# print(b'ab' + 'cd')                         # TypeError: can't concat str to bytes

print(b'ab'.decode() + 'cd')                  # bytes to str

print(b'ab' + 'cd'.encode())                  # str to bytes

print(b'ab' + bytes('cd', 'ascii'))           # str to bytes
