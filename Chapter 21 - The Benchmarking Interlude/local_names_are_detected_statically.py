X = 99

def selector():         # X used but not assigned
    print(X)        # X found in global scope

selector()

def selector():
    print(X)        # Does not yet exist!
    X = 88      # X classified as a local name (everywhere)
                # Can also happen for "import X", "def X"...

# selector()

def selector():
    global X        # Force X to be global (everywhere)
    print(X)
    x = 88

selector()

X = 99

def selector():
    import __main__         # Import enclosing module
    print(__main__.X)       # Qualify to get to global version of name
    X = 88          # Unqualified X classified as local
    print(X)        # Prints local version of name

selector()