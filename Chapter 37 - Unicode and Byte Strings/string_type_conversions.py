S = 'eggs'

print(S.encode())               # str->bytes: encode text into raw bytes

print(bytes(S, encoding = 'ascii'))     # str->bytes, alternative

B = b'spam'

print(B.decode())               # bytes->str: decode raw bytes into text

print(str(B, encoding = 'ascii'))       # bytes->str, alternative

import sys

print(sys.platform)

print(sys.getdefaultencoding())

# print(bytes(S))                 # TypeError: string argument without an encoding

print(str(B))                     # str without encoding

print(len(str(B)))

print(len(str(B, encoding = 'ascii')))
