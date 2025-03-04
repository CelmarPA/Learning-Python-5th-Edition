class Tracer:
    def __init__(self, aClass):                             # On @decorator
        self.aClass = aClass                                # Use instance attribute

    def __call__(self, *args):                              # On instance creation
        self.wrapped = self.aClass(*args)                   # ONE (LAST) INSTANCE PER CLASS!
        return self

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

@Tracer                                                     # Triggers __init__
class Spam:                                                 # Like: Spam = Tracer(Spam)
    def display(self):
        print('Spam!' * 8)

food = Spam()                                               # Triggers __call__
food.display()                                              # Triggers __getattr__

print('-' * 80)

@Tracer
class Person:                                               # Person = Tracer(Person)
    def __init__(self, name):                               # Wrapper bound to Person
        self.name = name

bob = Person('Bob')                                         # bob is really a Wrapper
print(bob.name)                                             # Wrapper embeds a Person
sue = Person('Sue')
print(sue.name)                                             # sue overwrites bob
print(bob.name)                                             # OOPS: now bob's name is 'Sue'!
