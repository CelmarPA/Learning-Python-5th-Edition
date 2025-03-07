class MetaOne(type):
    def __new__(meta, classname, supers, classdict):                            # Redefine type method
        print('In MetaOne.new: ', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        return 'toast'

class Super(metaclass = MetaOne):                                               # Metaclass inherited by subs too
    def spam(self):                                                             # MetaOne run twice for two classes
        return 'spam'

class Sub(Super):                                                               # Superclass: inheritance versus instance
    def eggs(self):                                                             # Classes inherit from superclasses
        return 'eggs'                                                           # But not from metaclasses

# from metainstance import *                                                      # Runs class statements: metaclass run twice

X = Sub()                                                                       # Normal instance of user-defined class
print(X.eggs())                                                                 # Inherited from Sub

print(X.spam())                                                                 # Inherited from Super

# print(X.toast())                                                                # AttributeError: 'Sub' object has no attribute 'toast'                                                          # Not inherited from metaclass

print(Sub.toast)

print(Sub.spam)

print(X.spam)
