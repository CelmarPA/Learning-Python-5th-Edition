B = b'A\xc3\x84B\xc3\xa8C'          # Text encoded in UTF-8 format originally

print(B)

S = B.decode('utf-8')               # Decode to Unicode text per UTF-8

print(S)

T = S.encode('cp500')               # Convert to encoded bytes per EBCDIC

print(T)

U = T.decode('cp500')               # Convert back to Unicode per EBCDIC

print(U)

print(U.encode())                   # Per default utf-8 encoding again
