S = 'A\u00c4B\U000000e8C'

print(S)                        # A, B, C, and 2 non-ASCII characters

print(len(S))                   # Five characters long

print(S.encode('latin-1'))

print(len(S.encode('latin-1')))     # 5 bytes when encoded per latin-1

S.encode('utf-8')

print(len(S.encode('utf-8')))       # 7 bytes when encoded per utf-8

S = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

print(S)

print(S.encode('cp500'))            # Two other Western European encodings

print(S.encode('cp850'))            # 5 bytes each, different encoded values

S = 'spam'                          # ASCII text is the same in most

print(S.encode('latin-1'))

print(S.encode('utf-8'))

print(S.encode('cp500'))             # But not in cp500: IBM EBCDIC!

print(S.encode('cp850'))

S= 'A\u00c4B\U000000e8C'

print(S)

print(S.encode('utf-16'))

S = 'spam'

print(S.encode('utf-16'))

print(S.encode('utf-32'))

