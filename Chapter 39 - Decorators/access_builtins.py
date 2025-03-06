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