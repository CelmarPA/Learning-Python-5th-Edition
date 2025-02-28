from __future__ import print_function

from validate_tester import loadClass

CardHolder = loadClass()

bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main str')
print('bob:', bob.name, bob.acct, bob.age, bob.addr)

sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main str')
print('sue:', sue.name, sue.acct, sue.age, sue.addr)            # addr differs: client data
print('bob:', bob.name, bob.acct, bob.age, bob.addr)            # name,acct,age overwritten?

# command-line: py −3 validate_tester2.py validate_descriptors1
# command-line: py −3 validate_tester2.py validate_descriptors2
# command-line: py −3 validate_tester2.py validate_getattr
# command-line: py −3 validate_tester2.py validate_getattribute
