class Person:
    def __init__(self, name):
        self._name = name

    def __getattribute__(self, attr):                   # On [obj.any]
        print('get: ' + attr)
        if attr == 'name':                              # Intercept all names
            attr = '_name'                              # Map to internal name
        return object.__getattribute__(self, attr)      # Avoid looping here

    def __setattr__(self, attr, value):                 # On [obj.any = value]
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                              # Set internal name
        self.__dict__[attr] = value                     # Avoid looping here

    def __delattr__(self, attr):                        # On [del obj.any]
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                              # Avoid looping here too
        del self.__dict__[attr]                         # but much less common

bob = Person('Bob Smith')                       # bob has a managed attribute

print(bob.name)                                 # Runs __getattr__

bob.name = 'Robert Smith'                       # Runs __setattr__

print(bob.name)

del bob.name

print('-' * 20)

sue = Person('Sue Jones')                       # sue inherits property too

print(sue.name)

# print(Person.name.__doc__)                    # No equivalent here
