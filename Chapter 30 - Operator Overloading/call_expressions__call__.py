class Callee:
    def __call__(self, *pargs, **kargs):            # Intercept instance calls
        print('Called:', pargs, kargs)              # Accept arbitrary arguments

C = Callee()

C(1, 2, 3)                                    # C is a callable object

C(1, 2, 3, x = 4, y = 5)

class Prod:
    def __init__(self, value):          # Accept just one argument
        self.value = value

    def __call__(self, other):
        return self.value * other

x = Prod(2)                             # "Remembers" 2 in state

print(x(3))                             # 3 (passed) * 2 (state)

print(x(4))

class Prod:
    def __init__(self, value):
        self.value = value

    def comp(self, other):
        return self.value * other

x = Prod(3)

print(x.comp(3))

print(x.comp(4))
