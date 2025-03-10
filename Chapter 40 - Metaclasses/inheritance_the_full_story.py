class M1(type): attr1 = 1               # Metaclass inheritance tree
class M2(M1): attr2 = 2                 # Gets __bases__, __class__, __mro__

class C1: attr3 = 3                     # Superclass inheritance tree
class C2(C1, metaclass = M2): attr4 = 4 # Gets __bases__, __class__, __mro__

I = C2()                                # I gets __class__ but not others
print(I.attr3, I.attr4)                 # Instance inherits from super tree

print(C2.attr1, C2.attr2, C2.attr3, C2.attr4)       # Class gets names from both trees!

print(M2.attr1, M2.attr2)                           # Metaclass inherits names too!

print(I.__class__)                      # Links followed at instance with no __bases__

print(C2.__bases__)

print(C2.__class__)                     # Links followed at class after __bases__

print(M2.__bases__)

print(I.__class__.attr1)                # Route inheritance to the class's meta tree

# print(I.attr1)                          # Though class's __class__ not followed normally

print([x.__name__ for x in C2.__mro__])     # __bases__ tree from I.__class__

print([x.__name__ for x in M2.__mro__])     # __bases__ tree from C2.__class__
