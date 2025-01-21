"""
reloadall2.py: transitively reload nested modules (alternative coding)
"""

import types
from importlib import reload

def status(module):
    print('reloading ' + module.__name__)

def tryreload(module):
    try:
        reload(module)
    except:
        print("FAILED: %s" % module)

def tester(reloader, modname):      # Self-test code
    import importlib, sys       # Import on tests only
    if len(sys.argv) > 1: modname = sys.argv[1]         # command line (or passed)
    module = importlib.import_module(modname)       # Import by name string
    reloader(module)

def transitive_reload(objects, visited):
    for obj in objects:
        if type(obj) == types.ModuleType and obj not in visited:
            status(obj)
            tryreload(obj)      # Reload this, recur to attrs
            visited.add(obj)
            transitive_reload(obj.__dict__.values(), visited)

def reload_all(*args):
    transitive_reload(args, set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall2')
