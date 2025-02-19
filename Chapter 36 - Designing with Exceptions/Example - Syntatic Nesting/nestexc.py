def action2():
    print(1+ [])                    # Generate TypeError

def action1():
    try:
        action2()
    except TypeError:               # Most recent matching try
        print('inner try')

try:
    try:
        action2()
    except TypeError:               # Most recent matching try
        print('inner try')
except TypeError:                   # Here, only if nested handler re-raises
    print('outer try')

try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')