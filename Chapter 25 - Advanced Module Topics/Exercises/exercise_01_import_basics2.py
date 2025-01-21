def countLines(name):
    tot = 0
    for line in open(name): tot += 1
    return tot

def countChars(name):
    tot = 0
    for line in open(name): tot += len(line)
    return tot


def test(name):
    print(countLines(name), countChars(name))
    return countLines(name), countChars(name)

"""
import exercise_01_import_basics

test(exercise_01_import_basics.__file__)
"""