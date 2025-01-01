class Tester:       # Class-based alternative
    def __init__(self, start):      # On object construction,
        self.state = start      # save state explicitly in new object
    def nested(self, label):
        print(label, self.state)        # Reference state explicitly
        self.state += 1     # Changes are always allowed

F = Tester(0)       # Create instance, invoke __init__
F.nested('spam')        # F is passed to self
F.nested('ham')

G = Tester(42)
G.nested('toast')
G.nested('bacon')

F.nested('eggs')

print(F.state)

class Tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):      # Intercept direct instance calls
        print(label, self.state)        # So .nested() not required
        self.state += 1

H = Tester(99)
H('juice')      # Invokes __call__
H('pancakes')
