def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c = 3)

kwonly(a = 1, c = 3)

# kwonly(1, 2, 3)

def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c = 3, b = 2)

kwonly(c = 3, b = 2, a = 1)

# kwonly(1, 2, 3)

def kwonly(a, *, b = 'spam', c = 'ham'):
    print(a, b, c)

kwonly(1)

kwonly(1, c = 3)

kwonly(a = 1)

kwonly(c = 3, b = 2, a = 1)

# kwonly(1 , 2)

def kwonly(a, *, b, c = 'spam'):
    print(a, b, c)

kwonly(1, b = 'eggs')

# kwonly(1, c = 'eggs')

def kwonly(a, *, b = 1, c, d = 2):
    print(a, b, c, d)

kwonly(3 ,c = 4)

kwonly(3, c = 4, b = 5)

# kwonly(3)

# def f(a, *b, **d, c = 6): print(a, b, c, d) # Keyword-only before **!

def f(a, *b, c = 6, **d): print(a, b, c, d)     # Collect args in header

f(1, 2, 3, x = 4, y = 5)        # Default used

f(1, 2, 3, x = 4, y = 5, c = 7)     # Override default

f(1, 2, 3, c = 7, x = 4, y = 5)     # Anywhere in keywords

def f(a, c = 6, *b, **d): print(a, b, c, d)     # c is not keyword-only here!

f(1, 2, 3, x = 4)

def f(a, *b, c = 6, **d): print(a, b, c, d)     # KW-only between * and **

f(1, *(2, 3), **dict(x = 4, y = 5))     # Unpack args at call

f(1, *(2, 3), **dict(x = 4, y = 5), c = 7)      # Keywords before **args!

f(1, *(2, 3), c = 7, **dict(x = 4, y = 5))      # Override default

f(1, c=7, *(2, 3), **dict(x = 4, y = 5))        # After or before *

f(1, *(2, 3), **dict(x = 4, y = 5, c = 7))      # Keyword-only in **

