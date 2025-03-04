class Wrapper:
    def __init__(self, object):
        self.wrapped = object                       # Save object

    def __getattr__(self, attrname):
        print('Trace:', attrname)                   # Trace fetch
        return getattr(self.wrapped, attrname)      # Delegate fetch

x = Wrapper([1, 2, 3])                              # Wrap a list

x.append(4)                                         # Delegate to list method

print(x.wrapped)                                    # Print my member

x = Wrapper({"a": 1, "b": 2})                       # Wrap a dictionary

print(list(x.keys()))                               # Delegate to dictionary method

print('-' * 80)

# Tracing interfaces with class decorators

def Tracer(aClass):                                 # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs):         # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)   # Use enclosing scope name

        def __getattr__(self, attrname):
            print('Trace: ' + attrname)             # Catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)  # Delegate to wrapped obj

    return Wrapper

if __name__ == '__main__':
    @Tracer
    class Spam:                                     # Spam = Tracer(Spam)
        def display(self):                          # Spam is rebound to Wrapper
            print('Spam!' * 8)

    @Tracer
    class Person:                                   # Person = Tracer(Person)
        def __init__(self, name, hours, rate):      # Wrapper remembers Person
            self.name = name
            self.hours = hours
            self.rate = rate

        def pay(self):                              # Accesses outside class traced
            return self.hours * self.rate           # In-method accesses not traced

    food = Spam()                                   # Triggers Wrapper()
    food.display()                                  # Triggers __getattr__
    print([food.fetches])

    bob = Person('Bob', 40, 50)    # bob is really a Wrapper
    print(bob.name)                                 # Wrapper embeds a Person
    print(bob.pay())

    print('')

    sue = Person('Sue', rate = 100, hours = 60)     # sue is a different Wrapper
    print(sue.name)                                       # with a different Person
    print(sue.pay())

    print(bob.name)                                       # bob has different state
    print(bob.pay())
    print([bob.fetches, sue.fetches])                     # Wrapper attrs not traced
