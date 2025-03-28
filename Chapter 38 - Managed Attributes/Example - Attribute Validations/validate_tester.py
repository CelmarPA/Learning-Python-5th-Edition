from __future__ import print_function

def loadClass():
    import sys, importlib
    modulename = sys.argv[1]                            # Module name in command line
    module = importlib.import_module(modulename)        # Import module by name string
    print('[Using: %s' % module.CardHolder)             # No need for getattr() here
    return module.CardHolder

def printHolder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep = ' / ')

if __name__ == '__main__':
    CardHolder = loadClass()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printHolder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    printHolder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printHolder(sue)

    try:
        sue.age = 200
    except:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')

# command-line: py −3 validate_tester.py validate_properties
# command-line: py −3 validate_tester.py validate_descriptors1
# command-line: py −3 validate_tester.py validate_getattr
# command-line: py −3 validate_tester.py validate_getattribute
