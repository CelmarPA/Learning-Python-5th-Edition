# Database script to print and update shelve created in the prior script "example_11"

import shelve

db = shelve.open('dbfile')

for key in db:
    print(key, '=>', db[key])

bob = db['bob']
bob['age'] += 1

db['bob'] = bob
db.close()
