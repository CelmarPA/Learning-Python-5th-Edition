from . import m1

#import m1

# import dualpkg.m1 as m1         # And: set PYTHONPATH=c:\code

def somefunc():
    m1.somefunc()
    print('m2.somefunc')

if __name__ == '__main__':
    somefunc()          # Self-test or top-level script usage mode code
