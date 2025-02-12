class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)

a = Spam()                                                                    # Can call functions in class in 3.X
b = Spam()                                                                    # Calls through instances still pass a self
c = Spam()

Spam.printNumInstances()                        # Differs in 3.X

# a.printNumInstances()              # TypeError: Spam.printNumInstances() takes 0 positional arguments but 1 was given
