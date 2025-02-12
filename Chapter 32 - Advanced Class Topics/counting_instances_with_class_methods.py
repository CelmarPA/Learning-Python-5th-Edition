class Spam:
    numInstances = 0                                                # Use class method instead of static
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances(cls):
        print("Number of instances: %s" % cls.numInstances)

    printNumInstances = classmethod(printNumInstances)

a, b = Spam(), Spam()

a.printNumInstances()                                               # Passes class to first argument

Spam.printNumInstances()                                            # Also passes class to first argument