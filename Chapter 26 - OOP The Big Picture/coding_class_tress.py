class C2:       # Make class objects (ovals)
    def __init__(self):
        self.x = 1
        self.z = 2

class C3:
    def __init__(self):
        self.w = 3
        self.z = 4

class C1(C2, C3):       # Linked to superclasses (in this order)
    def __init__(self):
        self.name = None
        self.x = 2
        self.y = 5


    def setName(self, who):      # Assign name: C1.setName
        self.name = who     # Self is either I1 or I2

I1 = C1()       # Make instance objects (rectangles)

I2 = C1()       # Linked to their classes

I1.setName('bob')       # Sets I1.name to 'bob'

I2.setName('sue')

print(I1.name)
