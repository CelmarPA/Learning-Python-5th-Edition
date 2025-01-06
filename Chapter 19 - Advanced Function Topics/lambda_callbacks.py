import sys
from tkinter import Button, mainloop        # Tkinter in 2.X

x = Button(
    text = 'Press me',
    command = (lambda: sys.stdout.write('Spam\n')))     # 3.X: print()

x.pack()
mainloop()      # This may be optional in console mode

class MyGui:
    def makewidgets(self):
        Button(command = (lambda: self.onPress("spam")))
    def onPress(self, message):
            print(message)