# The Basics

class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)

    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()

X.job                       # Prints "Get: job"

X.pay                       # Prints "Get: pay"

X.pay = 99                  # Prints "Set: pay 99"

print('-' * 80)

class Catcher:
    def __getattribute__(self, name):               # Works same as getattr here
        print('Get: %s' % name)                     # But prone to loops on general

    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()

X.job                       # Prints "Get: job"

X.pay                       # Prints "Get: pay"

X.pay = 99                  # Prints "Set: pay 99"

print('-' * 80)

class Wrapper:
    def __init__(self, object):
        self.wrapped = object                       # Save object

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)                 # Trace fetch
        return getattr(self.wrapped, attrname)      # Delegate fetch

X = Wrapper([1, 2, 3])

X.append(4)             # Prints "Trace: append"

print(X.wrapped)        # Prints "[1, 2, 3, 4]"
