def func(a, b, c, e = True, f = None):              # Args: three required, two defaults
    x = 1                                           # Plus two more local variables
    y = 2

code = func.__code__                                # Code object of a function object

print(code.co_nlocals)

print(code.co_varnames)                             # All local variable names

print(code.co_varnames[:code.co_argcount])          # <== First N locals are expected args

def catcher(*pargs, **kargs): print('%s, %s' % (pargs, kargs))

catcher(1, 2, 3, 4, 5)

catcher(1, 2, c = 3, d = 4, e = 5)           # Arguments at calls

import sys

print(tuple(sys.version_info))

code = func.__code__ if sys.version_info[0]  == 3 else func.func_code

