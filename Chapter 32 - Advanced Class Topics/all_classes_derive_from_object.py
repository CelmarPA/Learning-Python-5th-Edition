class C: pass                       # For new-style classes

X = C()

print(type(X), type(C))             # Type is class instance was created from

print(isinstance(X, object))

print(isinstance(C, object))        # Classes always inherit from object

print(type('spam'), type(str))

print(isinstance('spam', object))   # Same for built-in types (classes)

print(isinstance(str, object))

print(type(type))                   # All classes are types, and vice versa

print(type(object))

print(isinstance(type, object))     # All classes derive from object, even type

print(isinstance(object, type))     # Types make classes, and type is a class

print(type is object)
