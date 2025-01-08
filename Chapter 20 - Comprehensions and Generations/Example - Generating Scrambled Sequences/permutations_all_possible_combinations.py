from scramble import scramble
from permute import permute1, permute2

print(list(scramble('abc')))       # Simple scrambles: N

print(permute1('abc'))        # Permutations larger: N!

print(list(permute2('abc')))        # Generate all combinations

G = permute2('abc')         # Iterate (iter() not needed)

print(next(G))

print(next(G))

for x in permute2('abc'): print(x)


print(permute1('spam') == list(permute2('spam')))

print(len(list(permute2('spam'))), len(list(scramble('spam'))))

print(list(scramble('spam')))

print(list(permute2('spam')))
