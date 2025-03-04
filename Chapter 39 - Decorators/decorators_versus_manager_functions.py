instances = {}

def getInstance(aClass, *args, **kwargs):
    if aClass not in instances:
        instances[aClass] = aClass(*args, **kwargs)
    return instances[aClass]

class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

bob = getInstance(Person, 'Bob', 40 , 10)              # Versus: bob = Person('Bob', 40, 10)

print('-' * 80)

instances = {}

def getInstance(object):
    aClass = object.__class__
    if aClass not in instances:
        instances[aClass] = object
    return instances[aClass]

bob = getInstance(Person('Bob', 40 ,10))      # Versus: bob = Person('Bob', 40, 10)
