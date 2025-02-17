from setwrapper import Set

x = Set([1, 2, 3, 4])

y = Set([3, 4, 5])

print(x & y)
print(x | y)

z = Set('hello')

print(z[0], z[-1], z[2:])

for c in z:
    print(c, end = ' ')

print()

print(''.join(c.upper() for c in z))

print(len(z), z)

print(z & 'mello', z | 'mello')

class MultiSet(Set):
    """
    Inherits all Set names, but extends intersect and union to support
    multiple operands; note that "self" is still the first argument
    (stored in the *args argument now); also note that the inherited
    & and | operators call the new methods here with 2 arguments, but
    processing more than 2 requires a method call, not an expression;
    intersect doesn't remove duplicates here: the Set constructor does;
    """
    def intersect(self, *others):
        res = []
        for x in self:
            for other in others:
                if x not in other: break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)

x = MultiSet([1, 2, 3, 4])
y = MultiSet([3, 4, 5])
z = MultiSet([0, 1, 2])

print(x & y, x | y)

print(x.intersect(y, z))

print(x.union(y, z))

print(x.intersect([1, 2, 3], [2, 3, 4], [1, 2, 3]))

print(x.union(range(10)))

w = MultiSet('spam')

print(w)

print(''.join(w | 'super'))

print((w | 'super') & MultiSet('slots'))
