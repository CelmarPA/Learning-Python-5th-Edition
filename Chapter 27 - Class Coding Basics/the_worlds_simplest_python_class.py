class Rec: pass             # Empty namespace object

Rec.name = 'Bob'            # Just objects with attributes
Rec.age = 40

print(Rec.name)             # Like a C struct or a record

x = Rec()                   # Instances inherit class names
y = Rec()

print(x.name, y.name)       # name is stored on the class only

x.name = 'Sue'              # But assignment changes x only

print(Rec.name, x.name, y.name)

print(list(Rec.__dict__.keys()))

print(list(name for name in Rec.__dict__ if not name.startswith('__')))

print(list(x.__dict__.keys()))

print(list(y.__dict__.keys()))      # list() not required in Python 2.X

print(x.name, x.__dict__['name'])           # Attributes present here are dict keys

print(x.age)            # But attribute fetch checks classes too

# print(x.__dict__['age'])            # Indexing dict does not do inheritance

print(x.__class__)          # Instance to a class link

print(Rec.__bases__)

def upperName(obj):
    return obj.name.upper()         # Still needs a self-argument (obj)

print(upperName(x))

Rec.method = upperName          # Now it's a class's method!

print(x.method())               # Run method to process x

print(y.method())               # Same, but pass y to self

print(Rec.method(x))            # Can call through instance or class
