from listinstance import ListInstance

class Spam(ListInstance):                       # Inherit a __str__ method
    def __init__(self):
        self.data = 'food'

x = Spam()

print(x)

display = str(x)                                # Print this to interpret escapes

print(display)

print(x)                                        # The __repr__ still is a default
