import re

S = 'Bugger all down here on earth!'            # Line of text

B = b'Bugger all down here on earth!'           # Usually from a file

txt = re.match('(.*) down (.*) on (.*)', S).groups()        # Match line to pattern

print(txt)                                      # Matched substrings

txt = re.match(b'(.*) down (.*) on (.*)', B).groups()       # bytes substrings

print(txt)

B = bytearray(B)

txt = re.match(b'(.*) down (.*) on (.*)', B).groups()

print(txt)
