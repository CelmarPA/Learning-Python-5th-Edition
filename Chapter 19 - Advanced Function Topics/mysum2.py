def mysum(l):
    return 0 if not l else l[0] + mysum(l[1:])      # Use ternary expression

s = mysum([1, 2, 3, 4, 5])
print(s)

def mysum(l):
    return l[0] if len(l) == 1 else l[0] + mysum(l[1:])     # Any type, assume one

s = mysum([1, 2, 3, 4, 5])
print(s)

def mysum(l):
    first, *rest = l
    return first if not rest else first + mysum(rest)       # Use 3.X ext seq assign

s = mysum([1, 2, 3, 4, 5])
print(s)

print(mysum([1]))       # mysum([]) fails in last 2
print(mysum([1, 2, 3, 4, 5]))
print(mysum(('s', 'p', 'a', 'm')))      # But various types now work
print(mysum(['spam', 'ham', 'eggs']))
print(mysum('spam'))

def mysum(l):
    if not l: return 0
    return nonempty(l)      # Call a function that calls me

def nonempty(l):
    return l[0] + mysum(l[1:])      # Indirectly recursive

print(mysum([1.1, 2.2, 3.3, 4.4]))
