def printNumInstances():
    print("Number of instances created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

a = Spam()
b = Spam()
c = Spam()

printNumInstances()                 # But function may be too far removed

print(Spam.numInstances)            # And cannot be changed via inheritance

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances(self):
        print("Number of instances created: %s" % Spam.numInstances)

a, b, c = Spam(), Spam(), Spam()

a.printNumInstances()

Spam.printNumInstances(a)

Spam().printNumInstances()              # But fetching counter changes counter!
