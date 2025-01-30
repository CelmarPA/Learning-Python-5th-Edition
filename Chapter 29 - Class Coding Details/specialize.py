class Super:
    def method(self):
        print('in Super.method')            # Default behavior
    def delegate(self):
        self.action()                       # Expected to be defined

class Inheritor(Super):                     # Inherit method verbatim
    pass

class Replacer(Super):                      # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super):                      # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):                      # Fill in a required method
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined!'             # If this version is called

"""
X = Super()
X.delegate()            # AssertionError: action must be defined!
"""

class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

"""
X = Super()
X.delegate()        # NotImplementedError: action must be defined!
"""

class Sub(Super): pass

"""
X = Sub()
X.delegate()        # NotImplementedError: action must be defined!
"""

class Sub(Super):
    def action(self): print('spam')

X = Sub()
X.delegate()        # spam

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

# X = Super()           # TypeError: Can't instantiate abstract class Super with abstract methods action

class Sub(Super): pass

# X = Sub()             # TypeError: Can't instantiate abstract class Sub with abstract methods action

class Sub(Super):
    def action(self): print('spam')

X = Sub()
X.delegate()            # 'spam'
