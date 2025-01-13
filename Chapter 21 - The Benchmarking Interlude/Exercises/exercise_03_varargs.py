from warnings import simplefilter


def adder1(*args):
    print('adder1', end = ' ')
    if type(args[0]) == type(0):        # Integer?
        sum = 0         # Init to zero
    else:       # else sequence:
        sum = args[0][:0]       # Use empty slice of arg1
    for arg in args:
        sum = sum + arg
    return sum

def adder2(*args):
    print('adder2', end = ' ')
    sum = args[0]
    for next in args[1:]:
        sum += next
    return sum

for func in (adder1, adder2):
    print(func(2, 3, 4))
    print(func('spam', 'eggs', 'toast'))
    print(func(['a', 'b'], ['c', 'd'], ['e', 'f']))

# This solution won't work in dictionaries and mix types