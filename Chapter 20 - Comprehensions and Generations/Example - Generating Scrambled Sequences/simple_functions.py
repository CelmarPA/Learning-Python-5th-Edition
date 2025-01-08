def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append((seq[i:] + seq[:i]))
    return res

print(scramble('spam'))


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

print(scramble('spam'))

for x in scramble((1, 2, 3)):
    print(x, end = ' ')
