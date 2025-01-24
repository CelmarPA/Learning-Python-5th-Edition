rec = ('Bob', 40.5, ['dev', 'mgr'])         # Tuple-based record

print(rec[0])

rec = {}

rec['name'] = 'Bob'         # Dictionary-based record
rec['age'] = 40.5           # Or {...}, dict(n=v), etc.
rec['jobs'] = ['dev', 'mgr']

print(rec['name'])

class Rec: pass

Rec.name = 'Bob'        # Class-based record
Rec.age  = 40.5
Rec.jobs = ['dev', 'mgr']

print(Rec.name)

class Rec: pass

pers1 = Rec()           # Instance-based records

pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = Rec()

pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

print(pers1.name, pers2.name)

class Person:
    def __init__(self, name, jobs, age = None):         # class = data + logic
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs)

rec1 = Person('Bob', ['dev', 'mgr'], 40.5)      # Construction calls

rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs, rec2.info())       # Attributes + methods
