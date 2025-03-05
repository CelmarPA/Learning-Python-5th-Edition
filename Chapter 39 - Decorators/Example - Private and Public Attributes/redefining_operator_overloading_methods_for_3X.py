# Inline definition

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)

            # Intercept and delegate built-in operations specifically
            def __str__(self):
                return str(self.__wrapped)

            def __add__(self, other):
                return self.__wrapped + other

            def __getitem__(self, index):
                return self.__wrapped[index]

            def __call__(self, *args, **kargs):
                return self.__wrapped(*args, **kargs)
            # plus any other needed

            # Intercept and delegate by-name attribute access generically
            def __getattr__(self, attr): ...

            def __setattr__(self, attr, value): ...
        return onInstance
    return onDecorator

# Mix-in superclasses

class BuiltinsMixin:
    def __add__(self, other):
        return self.__class__.__getattr__(self, '__add__')(other)

    def __str__(self):
        return self.__class__.__getattr__(self, '__str__')()

    def __getitem__(self, index):
        return self.__class__.__getattr__(self, '__getitem__')(index)

    def __call__(self, *args, **kargs):
        return self.__class__.__getattr__(self, '__call__')(*args, *kargs)
    # plus any others needed

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance(BuiltinsMixin):
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)

            # Intercept and delegate built-in operations specifically
            def __str__(self):
                return str(self.__wrapped)

            def __add__(self, other):
                return self.__wrapped + other

            def __getitem__(self, index):
                return self.__wrapped[index]

            def __call__(self, *args, **kargs):
                return self.__wrapped(*args, **kargs)
            # plus any other needed

            def __getattr__(self, attr): ...

            def __setattr__(self, attr, value): ...

class BuiltinsMixin:
    def __add__(self, other):
        return self.__wrapped + other

    def __str__(self):
        return str(self.__wrapped)

    def __getitem__(self, index):
        return self.__wrapped[index]

    def __call__(self, *args, **kargs):
        return self.__wrapped(*args, **kargs)
    # plus any other needed

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance(BuiltinsMixin):
            def __init__(self, *args, **kargs):
                self._wrapped = aClass(*args, **kargs)

            # Intercept and delegate built-in operations specifically
            def __str__(self):
                return str(self._wrapped)

            def __add__(self, other):
                return self._wrapped + other

            def __getitem__(self, index):
                return self._wrapped[index]

            def __call__(self, *args, **kargs):
                return self._wrapped(*args, **kargs)

            # plus any other needed

            def __getattr__(self, attr): ...

            def __setattr__(self, attr, value): ...

# Coding variations: Routers, descriptors, automation.

class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):
        return self.reroute('__add__',other)

    def __str__(self):
        return self.reroute('__str__')

    def __getitem__(self, index):
        return self.reroute('__getintem__', index)

    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)
    # plus any others needed

class BuiltinsMixin:
    class ProxyDesc(object):
        def __init__(self, attrname):
            self.attrname = attrname

        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attrname)            # Assume a _wrapped

    builtins = ['add', 'str', 'getitem', 'call']                        # Plus any others

    for attr in builtins:
        exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))
