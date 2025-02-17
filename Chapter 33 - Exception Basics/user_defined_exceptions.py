class AlreadyGotOne(Exception): pass                # User-defined exception

def grail():
    raise AlreadyGotOne()                           # Raise an instance

try:
    grail()
except AlreadyGotOne:
    print('got exception')

class Career(Exception):
    def __str__(self): return 'So I become a waiter...'

raise Career()
