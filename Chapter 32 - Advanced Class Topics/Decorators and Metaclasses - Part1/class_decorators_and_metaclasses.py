def decorator(cls):                                         # On @ decoration
    class Proxy:
        def  __init__(self, *args):                         # On instance creation: make a cls
            self.wrapped = cls(*args)

        def __getattr__(self, name):                        # On attribute fetch: extra ops here
            return getattr(self.wrapped, name)
    return Proxy

@decorator
class C: ...                                                # Like C = decorator(C)

X = C()                                                     # Makes a Proxy that wraps a C, and catches later X.attr
