class C2:       # Make class objects (ovals)
    def __init__(self):
        self.x = 1
        self.z = 2

class C3:
    def __init__(self):
        self.w = 3
        self.z = 4

class C1(C2, C3):
    def __init__(self,  who):       # Set name when constructed
        self.name = who     # Self is either I1 or I2

I1 = C1('bob')      # Sets I1.name to 'bob'
I2 = C1('sue')      # Sets I2.name to 'sue'

print(I1.name)      # Prints 'bob'
