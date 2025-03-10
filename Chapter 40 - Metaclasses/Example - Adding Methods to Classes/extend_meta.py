# Extend with a metaclass - supports future changes better
from importlib.metadata import pass_none


def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass = Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2

class Client2(metaclass = Extender):
    value = 'ni?'

X = Client1('Ni!')

print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()

print(Y.eggs())
print(Y.ham('bacon'))

# Can also configure class based on runtime tests

def sometest(): pass

def someothertest(): pass

class MetaExtend(type):
    def __new__(meta, classname, supers, classdict):
        if sometest:
            classdict['eggs'] = 1
        else:
            classdict['eggs'] = 2

        if someothertest:
            classdict['ham'] = hamfunc
        else:
            classdict['ham'] = lambda *args: 'Not supported'

        return type.__new__(meta, classname, supers, classdict)

