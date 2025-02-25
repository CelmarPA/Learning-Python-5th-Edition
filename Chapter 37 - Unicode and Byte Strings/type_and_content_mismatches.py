# Types are not flexible for file content
open('temp5', 'w').write('abc\n')                   # Text mode makes and requires str

# open('temp5', 'w').write(b'abc\n')                  # TypeError: write() argument must be str, not bytes

open('temp5', 'wb').write(b'abc\n')                 # Binary mode makes and requires bytes

# open('temp5', 'wb').write('abc\n')                  # TypeError: a bytes-like object is required, not 'str'
