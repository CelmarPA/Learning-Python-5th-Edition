class Spam:
    def __init__(self):             # No __repr__ or __str__
        self.data1 = "food"

X = Spam()
print(X)                            # Default: class name + address (id)