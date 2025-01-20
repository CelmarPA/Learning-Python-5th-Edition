from unders import *        # Load non _X names only

print(a, c)

# print(_b)         # NameError: name '_b' is not defined

import unders

print(unders._b)        # But other importers get every name

from alls import *      # Load __all__ names only

print(a, _c)

# print(b)           # NameError: name 'b' is not defined

from alls import a, b, _c, _d       # But other importers get every name

print(a, b, _c, _d)

import alls

print(alls.a, alls.b, alls._c, alls._d)

