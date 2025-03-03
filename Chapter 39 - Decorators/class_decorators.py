def decorator(cls):                                             # On @ decoration
    class Wrapper:
        def __init__(self, *args):                              # On instance creation
            self.wrapped = cls(*args)

        def __getattr__(self, name):                            # On attribute fetch
            return getattr(self.wrapped, name)

    return Wrapper

@decorator
class C:                                                        # C = decorator(C)
    def __init__(self, x, y):                                   # Run by Wrapper.__init__
        self.attr = 'spam'

x = C(6, 7)                                               # Really calls Wrapper(6, 7)
print(x.attr)                                                   # Runs Wrapper.__getattr__, prints "spam"

print('-' * 80)

# Supporting multiple instances

class Decorator:
    def __init__(self, C):                                      # On @ decoration
        self.C = C

    def __call__(self, *args):                                  # On instance creation
        self.wrapped = self.C(*args)
        return self

    def __getattr__(self, attrname):                            # On atrribute fetch
        return getattr(self.wrapped, attrname)

@Decorator
class C: ...                                                    # C = Decorator(C)

x = C()
y = C()                                                         # Overwrites x!

def decorator(C):                                               # On @ decoration
    class Wrapper:
        def __init__(self, *args):                              # On instance creation: new Wrapper
            self.wrapped = C(*args)                             # Embed instance in instance

    return Wrapper

class Wrapper: ...

def decorator(C):                                               # On @ decoration
    def onCall(*args):                                          # On instance creation: new Wrapper
        return Wrapper(C(*args))                                # Embed instance in instance
    return onCall
