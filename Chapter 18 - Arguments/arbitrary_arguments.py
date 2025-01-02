# Headers: Collecting arguments
def f(*args): print(args)

f()
f(1)
f(1, 2, 3, 4)

def f(**args): print(args)

f()
f(a = 1, b = 2)

def f(a, *pargs, **kargs): print(a, pargs, kargs)

f(1, 2, 3, x = 1, y = 2 )

# Calls: Unpacking arguments
def func(a, b, c, d): print(a, b, c, d)

args = (1, 2)
args += (3, 4)
print(args)
func(*args)     # Same as func(1, 2, 3, 4)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
print(args)
func(**args)        # Same as func(a=1, b=2, c=3, d=4)

func(*(1, 2), **{'d': 4, 'c': 3})       # Same as func(1, 2, d=4, c=3)
func(1, *(2, 3), **{'d': 4})        # Same as func(1, 2, 3, d=4)
func(1, c = 3, *(2,), **{'d': 4})       # Same as func(1, 2, c=3, d=4)
func(1, *(2, 3), d = 4)       # Same as func(1, 2, 3, d=4)
func(1, *(2,), c=3, **{'d':4})      # Same as func(1, 2, c=3, d=4)