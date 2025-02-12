class Spam:
    numInstances = 0                                                        # Trace class passed in
    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))

    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):                                             # Override a class method
        print("Extra stuff...", cls)                                        # But call back to original
        Spam.printNumInstances()

    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass                                                     # Inherit class method verbatim

x = Sub()
y = Spam()

x.printNumInstances()                                                       # Call from subclass instance

Sub.printNumInstances()                                                     # Call from subclass itself

y.printNumInstances()                                                       # Call from superclass instance

z = Other()

z.printNumInstances()                                                       # Call from lower sub's instance
