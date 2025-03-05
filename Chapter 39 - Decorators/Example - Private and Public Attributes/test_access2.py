from access2 import Private, Public

@Private('age')                                 # Person = Private('age')(Person)
class Person:                                   # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age = age                          # Inside accesses run normally

X = Person('Bob', 40)

print(X.name)                                   # Outside accesses validated

X.name = 'Sue'

print(X.name)

# print(X.age)              # TypeError: private attribute fetch: age

# X.age = 'Tom'             # TypeError: private attribute change: age

@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

X = Person('Bob', 40)               # X is an onInstance

print(X.name)                                  # onInstance embeds Person

X.name = 'Sue'

print(X.name)

# print(X.age)                # TypeError: private attribute fetch: age

# X.age = 'Tom'               # TypeError: private attribute change: age

@Private('age')
class Person:
    def __init__(self):
        self.age = 42
    def __str__(self):
        return 'Person: ' + str(self.age)
    def __add__(self, yrs):
        self.age += yrs

X = Person()

X.__add__(10)                           # Though calls by name work normally

print(X._onInstance__wrapped.age)       # Break privacy to view result...
