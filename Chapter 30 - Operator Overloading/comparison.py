class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other

X = C()

print(X > 'ham')                                # True (runs __gt__)
print(X < 'ham')                                # False (runs __lt__)
