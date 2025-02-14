class C:
    shared = []                     # Class attribute
    def __init__(self):
        self.perobj = []            # Instance attribute

x = C()                             # Two instances
y = C()

print(y.shared, y.perobj)           # Implicitly share class attrs

x.shared.append('spam')             # Impacts y's view too!
x.perobj.append('spam')             # Impacts x's data only

print(x.shared, x.perobj)

print(y.shared, y.perobj)           # y sees change made through x

print(C.shared)                     # Stored on class and shared
