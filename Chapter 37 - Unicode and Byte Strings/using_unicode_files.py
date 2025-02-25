S = 'A\xc4B\xe8C'                           # Five-character decoded string, non-ASCII

print(S)

print(len(S))

# Encode manually with methods

L = S.encode('latin-1')                     # 5 bytes when encoded as latin-1

print(L)

print(len(L))

U = S.encode('utf-8')                       # 7 bytes when encoded as utf-8

print(U)

print(len(U))

print('-' * 80)

# Encoding automatically when written

open('latindata', 'w', encoding='latin-1').write(S)     # Write as latin-1

open('utf8data', 'w', encoding='utf-8').write(S)        # Write as utf-8

file = open('latindata', 'rb').read()

print(file)

file = open('utf8data', 'rb').read()

print(file)

print('-' * 80)

# File input decoding

# Decoding automatically when read

file = open('latindata', 'r', encoding='latin-1').read()            # Decoded on input

print(file)

file = open('utf8data', 'r', encoding='utf-8').read()               # Per encoding type

print(file)

X = open('latindata', 'rb').read()                                  # Manual decoding:

print(X.decode('latin-1'))                                          # Not necessary

X = open('utf8data', 'rb').read()

print(X.decode())                                                   # UTF-8 is default

print('-' * 80)

# Decoding mismatches

file = open(r'C:\Python312\python.exe', 'r')

# text = file.read()      # UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2: character maps
# to <undefined>

file = open(r'C:\Python312\python.exe', 'rb')

data = file.read()

print(data[:20])
