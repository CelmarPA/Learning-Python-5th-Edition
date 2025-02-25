# Dropping the BOM in Notepad

import sys
from email.encoders import encode_noop

print(sys.getdefaultencoding())

print(open('spam.txt', 'rb').read())            # ASCII (UTF-8) text file

print(open('spam.txt', 'r').read())             # Text mode translates line end

print(open('spam.txt', 'r', encoding='utf-8').read())

print('-' * 80)

# Dropping the BOM in Python

print(open('temp.txt', 'w', encoding='utf-8').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())            # No BOM

print(open('temp.txt', 'w', encoding='utf-8-sig').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())            # Wrote BOM

print(repr(open('temp.txt', 'r').read()))

print(repr(open('temp.txt', 'r', encoding='utf-8').read()))       # Keeps BOM

print(repr(open('temp.txt', 'r', encoding='utf-8-sig').read()))   # Skips BOM

print(open('temp.txt', 'w').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())                # Data without BOM

print(repr(open('temp.txt', 'r').read()))           # Either utf-8 works

print(repr(open('temp.txt', 'r', encoding='utf-8').read()))

print(repr(open('temp.txt', 'r', encoding='utf-8-sig').read()))

print(sys.byteorder)

print(open('temp.txt', 'w', encoding='utf-16').write('spam\nSPAM\n'))

print(open('temp.txt', 'rb').read())

print(repr(open('temp.txt', 'r', encoding='utf-16').read()))

print(open('temp.txt', 'w', encoding='utf-16-be').write('\ufeffspam\nSPAM\n'))

print(open('temp.txt', 'rb').read())

print(repr(open('temp.txt', 'r', encoding='utf-16').read()))

print(repr(open('temp.txt', 'r', encoding='utf-16-be').read()))

print(open('temp.txt', 'w', encoding='utf-16-le').write('SPAM'))

print(open('temp.txt', 'rb').read())            # OK if BOM not present or expected

print(open('temp.txt', 'r', encoding='utf-16-le').read())

print(open('temp.txt', 'r', encoding='utf-16').read())  # UnicodeDecodeError: 'utf-16' codec can't decode bytes in
# position 0-1: Stream does not start with BOM
