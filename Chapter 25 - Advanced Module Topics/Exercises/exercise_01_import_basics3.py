def countLines(name): return sum(+1 for line in open(name))

def countChars(name): return sum(len(line) for line in open(name))

def test(name):
    return countLines(name), countChars(name)
