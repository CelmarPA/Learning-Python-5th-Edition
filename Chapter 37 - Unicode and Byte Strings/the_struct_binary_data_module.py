from struct import pack, unpack

print(pack('>i4sh', 7, b'spam', 8))

B = pack('>i4sh', 7, b'spam', 8)

print(B)

vals = unpack('>i4sh', B)

print(vals)

#  vals = unpack('>i4sh', B.decode())  # TypeError: a bytes-like object is required, not 'str'

print('-' * 80)

# Write values to a packed binary file

F = open('data.bin', 'wb')                      # Open binary output file

data = pack('>i4sh', 7, b'spam', 8)     # Create packed binary data

print(data)

F.write(data)                                   # Write to the file

F.close()

# Read values from a packed binary file

F = open('data.bin', 'rb')                      # Open binary input file

data = F.read()                                 # Read bytes

print(data)

values = unpack('>i4sh', data)           # Extract packed binary data

print(values)                                   # Back to Python objects

print('-' * 80)

# Accessing bits of parsed integers

print(bin(values[0]))                           # Can get to bits in ints

print(values[0] & 0x01)                         # Test first (lowest) bit in int

print(values[0] | 0b1010)                       # Bitwise or: turn bits on

print(bin(values[0] | 0b1010))                  # 15 decimal is 1111 binary

print(bin(values[0] ^ 0b1010))                  # Bitwise xor: off if both true

print(bool(values[0] & 0b100))                  # Test if bit 3 is on

print(bool(values[0] & 0b1000))                 # Test if bit 4 is set

print('-' * 80)

# Accessing bytes of parsed strings and bits within them

print(values[1])

print(values[1][0])                             # bytes string: sequence of ints

print(values[1][1:])                            # Prints as ASCII characters

print(bin(values[1][0]))                        # Can get to bits of bytes in strings

print(bin(values[1][0] | 0b1100))               # Turn bits on

print(values[1][0] | 0b1100)
