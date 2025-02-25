import sys

print(sys.getdefaultencoding(), sys.getfilesystemencoding())

# Filenames: Text versus bytes

f = open('xxx\u00A5', 'w')          # Non-ASCII filename

f.write('\xA5999\n')                # Writes five characters

f.close()

print(open('xxx\u00A5').read())     # Text: auto-encoded

import glob                         # Filename expansion tool

print(glob.glob('*\u00A5'))         # Get decoded text for decoded text
