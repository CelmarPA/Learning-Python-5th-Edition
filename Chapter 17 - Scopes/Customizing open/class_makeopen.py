import builtins

class Makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self
    def __call__(self, *kargs, **pargs):
        print('Custom open call %r' % self.id, kargs, pargs)
        return self.original(*kargs, **pargs)

make_open = Makeopen('spam')

F = open('script2.py')

print(F.read())