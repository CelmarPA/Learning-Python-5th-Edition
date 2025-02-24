# Build GUI with tkinter (Tkinter in 2.X) with buttons that change color and grow
from importlib.util import LazyLoader
from tkinter import *
import random

fontSize = 25

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']

def replay(text):
    print(text)
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text = 'Popup', bg = 'black', fg =  color).pack()
    L.config(fg = color)

def timer():
    L.config(fg = random.choice(colors))
    win.after(250, timer)

def grow():
    global fontSize
    fontSize += 5
    L.config(font = ('arial', fontSize, 'italic'))
    win.after(1000, grow)

win = Tk()

L = Label(win, text = 'Spam',
          font = ('arial', fontSize, 'italic'), fg = 'yellow', bg = 'navy',
          relief = RAISED)

L.pack(side = TOP, expand = YES, fill = BOTH)

Button(win, text = 'press', command = (lambda: replay('red'))).pack(side = BOTTOM, fill = X)
Button(win, text = 'timer', command = timer).pack(side = BOTTOM, fill = X)
Button(win, text = 'grow', command = grow).pack(side = BOTTOM, fill = X)

win.mainloop()
