import sys

class MyError(Exception): pass

def oops():
    raise MyError('Spam!')

def doomed():
    try:
        oops()
    except IndexError:
        print('caught and index error', sys.exc_info()[0])
    except MyError as data:
        print('caught error!', MyError, data)
        # print('caught error', sys.exc_info()[:2])
    else:
        print('no error caught...')

if __name__ == '__main__':
    doomed()
