S = 'A\xC4B\xE8C'           # 3.X: str recognizes hex and Unicode escapes

print(S)

S = 'A\u00C4B\U000000E8C'

print(S)

B = b'A\xC4B\xE8C'

print(B)                    # bytes recognizes hex but not Unicode

B = b'A\xC4B\xE8C'

print(B)

print(B.decode('latin-1'))      # Decode as latin-1 to interpret as text

S = 'AÄBèC'                 # Chars from UTF-8 if no encoding declaration

print(S)

# B = b'AÄBèC'                #SyntaxError: bytes can only contain ASCII literal characters

B = b'A\xC4B\xE8C'          # Chars must be ASCII, or escapes

print(B)

print(B.decode('latin-1'))

print(S.encode())           # Source code encoded per UTF-8 by default

print(S.encode('utf-8'))    # Uses system default to encode, unless passed

print(B.decode())           # Raw bytes do not correspond to utf-8
# UnicodeDecodeError: 'utf8' codec can't decode bytes in position 1-2: ...
