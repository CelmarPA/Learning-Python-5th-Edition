# Similar to example_07, but use classes so each window has own state information

from tkinter import *
import random

class MyGui:
    """
    A GUI with buttons that change color and make the label grow.
    """

    colors = ['blue', 'green', 'orange', 'red', 'brown', 'yellow']

    def __init__(self, parent, title = 'popup'):
        parent.title(title)
        self.growing = False
        self.fontSize = 10
        self.lab = Label(parent, text = 'Gui1', fg = 'white', bg = 'navy')
        self.lab.pack(expand = YES, fill = BOTH)
        Button(parent, text = 'Spam', command = self.replay).pack(side = LEFT)
        Button(parent, text = 'Grow', command = self.grow).pack(side = LEFT)
        Button(parent, text = 'Stop', command = self.stop).pack(side = LEFT)

    def replay(self):
        "Change the button's color at random on Spam press"
        self.fontSize += 5
        color = random.choice(self.colors)
        self.lab.config(bg = color,
                        font = ('courier', self.fontSize, 'bold italic'))

    def grow(self):
        "Start making the label grow on Grow press"
        self.growing = True
        self.grower()

    def grower(self):
        if self.growing:
            self.fontSize += 5
            self.lab.config(font = ('courier', self.fontSize, 'bold'))
            self.lab.after(500, self.grower)

    def stop(self):
        "Stop the button growing on Stop press"
        self.growing = False

class MySubGui(MyGui):
    colors = ['black', 'purple']                # Customize to change color choices

MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()
