# Method insertion: rest of access2.py code as before

traceMe = False

def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get:', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)

        def setattributes(self, attr, value):
            trace('set:', attr)
            if failIf(attr):
                raise TypeError('private attribute change: ' + attr)
            else:
                return object.__setattr__(self, attr, value)

        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes
        return aClass
    return onDecorator

def Private(*attributes):
    return accessControl(failIf = (lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf = (lambda attr: attr not in attributes))
