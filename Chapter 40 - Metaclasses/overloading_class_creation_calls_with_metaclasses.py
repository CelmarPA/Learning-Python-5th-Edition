# Classes can catch calls too (but built-ins look in metas, not supers!)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep = '\n...')
        return type.__call__(meta, classname, supers, classdict)

    def __init__(Class,  classname, supers, classdict):
        print('In SuperMeta.init: ', classname, supers, classdict, sep = '\n...')
        print('...init class object: ', list(Class.__dict__.keys()))

print('making metaclass')
class SubMeta(type, metaclass = SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep = '\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init: ', classname, supers, classdict, sep = '\n...')
        print('...init class object: ', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass = SubMeta):              # Invoke SubMeta, via SuperMeta.__call__
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data: ', X.data, X.meth(2))

print('-' * 80)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):                           # By name, not built-in
        print('In SuperMeta.call: ', classname)
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(SuperMeta):                                   # Created by type default
    def __init__(Class, classname, supers, classdict):      # Overrides type.__init__
        print('In Submeta.init: ', classname)

print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)                                         # Not a data descriptor if found by name
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})      # Explicit calls work: class inheritance
print()
SubMeta('yyy', (), {})                        # But implicit built-in calls do not: type
