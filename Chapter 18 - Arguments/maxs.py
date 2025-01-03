def max1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg > res:
            res = arg
    return res

def max2(first, *rest):
    for arg in rest:
        if arg > first:
            first = arg
    return first

def max3(*args):
    tmp = list(args)
    tmp.sort()
    # return max(tmp)
    return tmp[-1]

print(max1(3, 4, 1, 2))
print(max2("bb", "aa"))
print(max3([2,2], [1,1], [3,3]))
