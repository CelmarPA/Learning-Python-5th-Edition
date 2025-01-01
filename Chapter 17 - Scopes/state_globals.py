def tester(start):
    global state        # Move it out to the module to change it
    state = start       # global allows changes in module scope
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')       # Each call increments shared global state
F('eggs')

G = tester(42)      # Resets state's single copy in global scope
G('toast')
G('bacon')

F('ham')        # But my counter has been overwritten!