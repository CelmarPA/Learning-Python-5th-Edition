from tkinter import Button


class Callback:
    def __init__(self, color):                  # Function + state information
        self.color = color

    def __call__(self):                         # Support calls with no arguments
        print('turn', self.color)

# Handlers
cb1 = Callback('blue')                          # Remember blue
cb2 = Callback('green')                         # Remember green

B1 = Button(command=cb1)                        # Register handlers
B2 = Button(command=cb2)

# Events
cb1()                                           # Prints 'turn blue'
cb2()                                           # Prints 'turn green'

def callback(color):                            # Enclosing scope versus attrs
    def oncall():
        print('turn', color)
    return oncall

cb3 = callback('yellow')                        # Handler to be registered

cb3()                                           # On event: prints 'turn yellow'

cb4 = (lambda color = 'red': print('turn ' + color))            # Defaults retain state too

cb4()

class Callback:
    def __init__(self, color):                  # Class with state information
        self.color = color

    def changeColor(self):                      # A normal named method
        print('turn', self.color)

cb1 = Callback('blue')
cb2 = Callback('yellow')

B1 = Button(command=cb1.changeColor)            # Bound method: reference, don't call
B2 = Button(command=cb2.changeColor)            # Remembers function + self pair

cb1 = Callback('blue')

obj = cb1.changeColor                           # Registered event handler

obj()                                           # On event prints 'turn blue'
