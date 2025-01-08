def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]         # Generator function
        yield seq       # Assignments work here

print(list(scramble('spam')))

def scramble(seq):
    for i in range(len(seq)):       # Generator function
        yield seq[i:] + seq[:i]         # Yield one item per iteration

print(list(scramble('spam')))       # list()generates all results

print(list(scramble((1, 2, 3))))        # Any sequence type works

for x in scramble((1, 2, 3)):
    print(x, end = ' ')         # for loops generate results
