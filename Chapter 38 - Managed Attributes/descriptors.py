# The Basics

class Descriptor:
    "docstring goes here"
    def __get__(self, instance, owner): ...         # Return attr value
    def __set__(self, instance, value): ...         # Return nothing (None)
    def __delete__(self, instance): ...             # Return nothing (None)

# Descriptor method arguments

class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep = '\n')

class Subject:
    attr = Descriptor()                             # Descriptor instance is class attr

X = Subject()

print(X.attr)

print(Subject.attr)
