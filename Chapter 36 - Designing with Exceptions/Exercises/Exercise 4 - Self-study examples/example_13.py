# Database script to populate and query a MySql database

from MySQLdb import Connect

conn = Connect(host = 'localhost', user = 'root', passwd = 'XXXXXXX')

curs = conn.cursor()

try:
    curs.execute('drop database testpeopledb')
except:
    pass                                                # Did not exist

curs.execute('create database testpeopledb')
curs.execute('use testpeopledb')
curs.execute('create table people (name char(30), job char(10), pay int(4))')

curs.execute('insert people values (%S, %S, %S)', ('Bob', 'dev', 50000))
curs.execute('insert people values (%S, %S, %S)', ('Sue', 'dev', 60000))
curs.execute('insert people values (%S, %S, %S)', ('Ann', 'mgr', 40000))

curs.execute('select * from people')

for row in curs.fetchall():
    print(row)

curs.execute('select * from people where name = %s', ('Bob',))
print(curs.description)

colNames = [desc[0] for desc in curs.description]

while True:
    print('-' * 30)
    row = curs.fetchone()
    if not row: break
    for (name, value) in zip(colNames, row):
        print('%s => %s' % (name, value))

conn.commit()               # Save inserted records
