def f(a, b, c): print(a, b, c)

f(1, 2, 3)

# keyword
f(c = 3, b = 2, a = 1)      # a gets 1 by position, b and c passed by name

f(1, c = 3, b = 2)

# Defaults
def f(a, b = 2, c = 3): print(a, b, c)      # a required, b and c optional

f(1)        # Use defaults
f(a = 1)
f(1, 4)     # Override defaults
f(1,4 ,5)

f(1, c = 6)     # Choose defaults