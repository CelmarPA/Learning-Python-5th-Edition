class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file

def parser():
    raise FormatError(42, file = 'spam.txt')            # When error found

try:
    parser()
except FormatError as X:
    print('Error at: %s %s' % (X.file, X.line))

class FormatError(Exception): pass                      # Inherited constructor

def parser():
    raise  FormatError(42, 'spam.txt')                  # No keywords allowed!

try:
    parser()
except FormatError as X:
    print('Error at:', X.args[0], X.args[1])            # Not specific to this app
