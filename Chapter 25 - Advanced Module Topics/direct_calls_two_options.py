modname = 'string'

string = __import__(modname)

print(string)

import importlib

modname = 'string'

string = importlib.import_module(modname)

print(string)