import shelve

db = shelve.open('persondb')                # Reopen the shelve

print(len(db))                              # Three 'records' stored

print(list(db.keys()))                      # keys is the index

bob = db['Bob Smith']                       # Fetch bob by key

print(bob)                                  # Runs __repr__ from AttrDisplay

print(bob.lastName())                       # Runs lastName from Person

for key in db:                              # Iterate, fetch, print
    print(key, '=>', db[key])

for key in sorted(db):
    print(key, '=>', db[key])               # Iterate by sorted keys
