class NumErr(Exception): pass
class Divzero(NumErr): pass
class Oflow(NumErr): pass
class Uflow(NumErr): pass

def func():
    ...
    raise Divzero()
