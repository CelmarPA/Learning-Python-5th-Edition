S = '\u00c4\u00e8'              # Non-ASCII text string, two characters long

print(S)

print(len(S))

# S.encode('ascii')               # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

print(S.encode('latin-1'))        # 1 byte per character when encoded

print(S.encode('utf-8'))          # 2 bytes per character when encoded

print(len(S.encode('latin-1')))   # 2 bytes in latin-1, 4 in utf-8

print(len(S.encode('utf-8')))

B = b'\xc4\xe8'                   # Text encoded per Latin-1

print(B)

print(len(B))                     # 2 raw bytes, two encoded characters

print(B.decode('latin-1'))        # Decode to text per Latin-1

B = b'\xc3\x84\xc3\xa8'           # Text encoded per UTF-8

print(len(B))                     # 4 raw bytes, two encoded characters

print(B.decode('utf-8'))          # Decode to text per UTF-8

print(len(B.decode('utf-8')))     # Two Unicode characters in memory
