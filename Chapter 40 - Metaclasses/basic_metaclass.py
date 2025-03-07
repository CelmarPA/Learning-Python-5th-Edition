class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # Run by inherited type.__call__
        return type.__new__(meta, classname, supers, classdict)


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep = '\n...')
        return type.__new__(meta, classname, supers, classdict)

class Eggs:
    pass

print('making class')

class Spam(Eggs, metaclass = MetaOne):                          # Inherits from Eggs, instance of MetaOne
    data = 1                                                    # Class data attribute
    def meth(self, arg):                                        # Class method attribute
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))

print('-' * 80)

# Customizing Construction and Initialization

class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', classname, supers, classdict, sep = '\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep = '\n...')
        print('...init class object', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass = MetaTwo):                              # Inherits from Eggs, instance of MetaTwo
    data = 1                                                        # Class data attribute
    def meth(self, arg):                                            # Class method attribute
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))

print('-' * 80)

# A simple function can serve as a metaclass too

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc:', classname, supers, classdict, sep = '\n...')
    return type(classname, supers, classdict)

class Eggs:
    pass

print('making class')

class Spam(Eggs, metaclass = MetaFunc):                 # Run simple function at end
    data = 1                                            # Function returns class
    def meth(self, arg):
        return self.data + arg

print('making instance')

X = Spam()

print('data:', X.data, X.meth(2))

print('-' * 80)

# A normal class instance can serve as a metaclass too

class MetaObj:
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call: ', classname, supers, classdict, sep = '\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new: ', classname, supers, classdict)
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init:', classname, supers, classdict, sep = '\n...')
        print('..init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass = MetaObj()):                    # MetaObj is normal class instance
    data = 1                                                # Called at end of statement
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))

print('-' * 80)

# Instances inherit from classes and their supers normally

class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print('In SuperMetaObj.call: ', classname, supers, classdict, sep = '\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print('In SubMetaObj.new: ', classname, supers, classdict, sep = '\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdic):
        print('In SubMetaObj.init: ', classname, supers, classdic)
        print('...init class object:', list(Class.__dict__.keys()))

class Spam(Eggs, metaclass = SubMetaObj()):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
