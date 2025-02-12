class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances +1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()                                                # Calls from classes and instances work

a.printNumInstances()
