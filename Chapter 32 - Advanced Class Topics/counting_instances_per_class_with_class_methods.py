class Spam:
    numInstances = 0
    def count(cls):                         # Per-class instance counters
        cls.numInstances += 1               # cls is lowest class above instance

    def __init__(self):
        self.count()                        # Passes self.__class__ to count

    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):                     # Redefines __init__
        Spam.__init__(self)

class Other(Spam):                          # Inherits __init__
    numInstances = 0

x = Spam()

y1, y2 = Sub(), Sub()

z1, z2, z3 = Other(), Other(), Other()

print(x.numInstances, y1.numInstances, z1.numInstances)                 # Per-class data!

print(Spam.numInstances, Sub.numInstances, Other.numInstances)
