# Global scope
x = 99      # x and func assigned in module: global

def func(y):        # y and z assigned in function: locals
    # Local scope
    z = x + y       # x is a global
    return z

print(func(1))      # func in module: result = 100
