"""
reloadall3.py: transitively reload nested modules (explicit stack)
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

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()
        status(next)
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
                       if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
