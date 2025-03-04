# Registering decorated objects to an API

from __future__ import print_function

registry = {}

def register(obj):                                  # Both class and func decorator
    registry[obj.__name__] = obj                    # Add to registry
    return obj                                      # Return obj itself, not a wrapper

@register
def spam(x):
    return (x ** 2)                                 # spam = register(spam)

@register
def ham(x):
    return (x ** 3)

@register
class Eggs:                                         # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)

print('Registry:')

for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))                                      # Invoke objects manually
print(ham(2))                                       # Later calls not intercepted

X = Eggs(2)
print(X)

print('\nRegistry calls:')

for name in registry:
    print(name, '=>', registry[name](2))            # Invoke from registry

print('-' * 80)

# Augmenting decorated objects directly

def decorate(func):
    func.marked = True                              # Assign function attribute for later use
    return func

@decorate
def spam(a, b):
    return a + b

print(spam.marked)

def annotate(text):                                 # Same, but value is decorator argument
    def decorate(func):
        func.label = True
        return func
    return decorate

@annotate('spam data')
def spam(a, b):
    return a + b

print(spam(1, 2), spam.label)
