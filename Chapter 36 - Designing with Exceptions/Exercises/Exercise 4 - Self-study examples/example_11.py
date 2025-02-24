# Database script to populate a shelve with Python objects

rec1 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 40.5}

rec2 = {'name': {'first': 'Sue', 'last': 'Jones'},
        'job': ['mgr'],
        'age': 35.0}

import shelve

db = shelve.open('dbfile')
db['bob'] = rec1
db['sue'] = rec2
db.close()
