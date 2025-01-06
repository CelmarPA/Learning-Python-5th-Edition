def echo(message):      # Name echo assigned to function object
    print(message)

echo('Direct call')     # Name echo assigned to function object

x = echo        # Now x references the function too
x('Indirect call')      # Call object through name by adding ()

def indirect(func, arg):
    func(arg)       # Call the passed-in object by adding ()

indirect(echo, 'Argument call')     # Pass the function to another function

schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]

for (func, arg) in schedule:
    func(arg)       # Call functions embedded in containers

def make(label):        # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam')        # Label in enclosing scope is retained
F('Ham!')       # Call the function that make returned
F('Eggs!')
