"""
FIle access1.py (3.X + 2.X)

Privacy for attributes fetched from class instances.
See self-test code at the end of the file for a usage example.

Decorator same as: Doubler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance,
and each onInstance instance embeds a Doubler instance.
"""

traceMe = False

def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):                                                         # privates in enclosing scope
    def onDecorator(aClass):                                                    # aClass in enclosing scope
        class onInsntace:                                                       # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):                                        # My attrs don't call getattr
                trace('get:', attr)                                       # Others assumed in wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):                                 # Outside accesses
                trace('set:', attr, value)                                # Others run normally
                if attr == 'wrapped':                                           # Allow my attrs
                    self.__dict__[attr] = value                                 # Avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)                          # Wrapped obj attrs
        return onInsntace                                                       # Or use __dict__
    return onDecorator

if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))

    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])

    # The following all succeed
    print(X.label)
    X.display(); X.double(); X.display()
    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Spam'
    Y.display()

    # The following all fail properly
    """
    print(X.size())
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    """
