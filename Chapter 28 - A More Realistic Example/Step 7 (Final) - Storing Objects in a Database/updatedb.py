# File updatedb.py: update a Person object on a database

import shelve

db = shelve.open('persondb')                # Reopen shelve with the same filename

for key in sorted(db):                      # Iterate to display database objects
    print(key, '\t\t=>', db[key])           # Prints with custom format

sue = db['Sue Jones']                       # Index by key to fetch

sue.giveRaise(.10)                          # Update in memory using class's method

db['Sue Jones'] = sue

db.close()
