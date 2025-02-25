# bytearrays in Action
import cmath
from os import O_RDWR

# Creation in 3.X: text/binary do not mix

S = 'spam'

# C = bytearray(S)                                # TypeError: string argument without an encoding

C = bytearray(S, 'latin-1')                       # A content-specific type in 3.X

print(C)

B = b'spam'                                        # b'..' != '..' in 3.X (bytes/str)

C = bytearray(B)

print(C)

# Mutable, but must assign ints, not strings

print(C[0])

# C[0] = 'x'                                        # TypeError: an integer is required

# C[0] = b'x'                                       # TypeError: an integer is required

C[0] = ord('x')                                     # Use ord() to get a character's ordinal

print(C)

C[1] = b'Y'[0]                                      # Or index a byte string

print(C)

# in bytes but not bytearray
print(set(dir(b'abc')) - set(dir(bytearray(b'abc'))))

# in bytearray but not bytes
print(set(dir(bytearray(b'abc'))) - set(dir(b'abc')))

# Mutable method calls

print(C)

# C.append(b'LMN')                                    # TypeError: 'bytes' object cannot be interpreted as an integer

C.append(ord('L'))

print(C)

C.extend(b'MNO')

print(C)

# Sequence operations and string methods

print(C)

print(C + b'!#')

print(C[0])

print(C[1:])

print(len(C))

# print(C.replace('xY', 'sp'))            # TypeError: a bytes-like object is required, not 'str'

print(C.replace(b'xY', b'sp'))

print(C)

print(C * 4)
