class ListTree:
    def __str__(self): ...

class Super:
    def __str__(self): ...

class Sub(ListTree, Super): ...                     # Get ListTree's __str__ by listing it first

x = Sub()                                           # Inheritance searches ListTree before Super

print('-' * 80)

class ListTree:
    def __str__(self): ...
    def other(self): ...

class Super:
    def __str__(self): ...
    def other(self): ...

class Sub(ListTree, Super):                         # Get ListTree's __str__ by listing it first
    other = Super.other                             # But explicitly pick Super's version of other
    def __init__(self):
        ...

x = Sub()                                           # Inheritance searches Sub before ListTree/Super
