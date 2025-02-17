from default_exception_handler import fetcher

x = 'spam'

try:
    print(fetcher(x, 3))
finally:                                    # Termination actions
    print('after fetch')

def after():
    try:
        fetcher(x, 3)
    finally:
        print('after fetch')
    print('after try?')

after()

def after():
    try:
        fetcher(x, 4)
    finally:
        print('after fetch')
    print('after try?')

after()
