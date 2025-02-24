print(ord('a'))

print(hex(97))

print(chr(97))

print(int(0xC4))

print(chr(196))

s = 'ni'

print(s.encode('ascii'), s.encode('latin1'), s.encode('utf8'))

print(s.encode('utf16'),  len(s.encode('utf16')))

print(s.encode('utf32'), len(s.encode('utf32')))
