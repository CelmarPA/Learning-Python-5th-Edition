import sys

def oops():
    raise IndexError()

def doomed():
    try:
        oops()
    except IndexError:
        print('caught an index error!', sys.exc_info()[0])
    else:
        print('no error caught...')

if __name__ == '__main__':
    doomed()
