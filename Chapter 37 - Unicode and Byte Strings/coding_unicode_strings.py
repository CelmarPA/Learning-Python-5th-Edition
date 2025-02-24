# Coding ASCII Text

print(ord('X'))         # 'X' is binary code point value 88 in the default encoding

print(chr(88))          # 88 stands for character 'X'

S= 'XYZ'                # A Unicode string of ASCII text

print(S)

print((len(S)))         # Three characters long

print([ord(c) for c in S])      # Three characters with integer ordinal values

print(S.encode('ascii'))        # Values 0..127 in 1 byte (7 bits) each

print(S.encode('latin-1'))      # Values 0..255 in 1 byte (8 bits) each

print(S.encode('utf-8'))        # Values 0..127 in 1 byte, 128..2047 in 2, others 3 or 4

print(S.encode('latin-1'))

print(S.encode('latin-1')[0])

print(list(S.encode('latin-1')))

# Coding Non-ASCII Text

print(chr(0xc4))                # 0xC4, 0xE8: characters outside ASCII's range

print(chr(0xe8))

S = '\xc4\xe8'                  # Single 8-bit value hex escapes: two digits

print(S)

S = '\u00c4\u00e8'              # 16-bit Unicode escapes: four digits each

print(S)

print(len(S))                   # Two characters long (not number of bytes!)

S = '\U000000c4\U000000e8'      # 32-bit Unicode escapes: eight digits each

print(S)
