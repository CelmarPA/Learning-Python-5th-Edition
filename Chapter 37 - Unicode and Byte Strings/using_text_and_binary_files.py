# Text File Basics

# Basic text files (and strings) work the same as in 2.X

file = open('temp', 'w')

size = file.write('abc\n')                          # Returns number of characters written

file.close()                                        # Manual close to flush output buffer

file = open('temp')                                 # Default mode is "r" (== "rt"): text input

text = file.read()

print(text)

# Text and Binary Modes

# Write and read a text file

open('temp2', 'w').write('abc\n')                   # Text mode output, provide a str

print(open('temp2', 'r').read())                    # Text mode input, returns a str

print(open('temp2', 'rb').read())                   # Binary mode input, returns a bytes

# Write and read truly binary data

print(open('temp3', 'wb').write(b'a\x00c'))         # Provide a bytes

print(open('temp3', 'r').read())                     # Receive a str

print(open('temp3', 'rb').read())

# bytearrays work too

BA = bytearray(b'\x01\x02\x03')

print(open('temp4', 'wb').write(BA))

print(open('temp4', 'r').read())

print(open('temp4', 'rb').read())
