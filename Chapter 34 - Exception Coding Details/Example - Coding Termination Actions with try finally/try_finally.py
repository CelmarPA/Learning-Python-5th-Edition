class MyError(Exception): pass

def stuff(file):
    raise MyError()

file = open('data', 'w')                    # Open an output file (this can fail too)

try:
    stuff(file)                             # Raises exception
finally:
    file.close()                            # Always close file to flush output buffers

print('not reached')                        # Continue here only if no exception
