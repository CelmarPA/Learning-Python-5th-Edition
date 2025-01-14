def countdown(x):
    if x >= 0:
        if x > 0:
            print(x, end = ' ')
            countdown(x - 1)
        else:
            print('stop')
    else:
        print(f'{x} => Negative numbers are not accepted!')

countdown(5)

countdown(10)

countdown(-1)


# Non-recursive options:

print(list(range(5, 0, -1)))

t = [print(i, end = ' ') for i in range(5, 0, -1)]

print('')

c = list(map(lambda x: print(x, end = ' '),range(5, 0, -1)))

print('')

def countdown2(n):      # Generator function, recursive
    if n >= 0:
        if n > 0:
            yield n
            for x in countdown2(n - 1): yield x
        else:
            yield 'stop'
    else:
        print(f'{n} => Negative numbers are not accepted!')

print(list(countdown2(5)))

# Non-recursive options:

def countdown3(n):          # Generator function, simpler
    if n >= 0:
        yield from range(n, 0, -1)      # for x in range(): yield x

print(list(countdown3(5)))

print(list(x for x in range(5, 0, -1)))         # Equivalent generator expression

print(list(range(5, 0, -1)))        # Equivalent non-generator form
