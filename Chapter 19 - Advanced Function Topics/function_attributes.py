def func(a):
    b = 'spam'
    return b * a

print(func)

func.count = 0
func.count += 1

print(func.count)

func.handles = 'Button-Press'

print(func.handles)

print(dir(func))