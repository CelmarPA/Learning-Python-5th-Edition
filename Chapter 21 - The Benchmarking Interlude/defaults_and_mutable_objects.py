def saver(x = []):      # Saves away a list object
    x.append(1)         # Changes same object each time!
    print(x)

saver([2])          # Default not used

saver()         # Default used

saver()         # Grows on each call!

saver()

def saver(x = None):
    if x is None:       # No argument passed?
        x = []      # No argument passed?
    x.append(1)         # Changes new list object
    print(x)

saver([2])

saver()

saver()

def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []

saver()

saver()

saver()
