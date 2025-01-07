print(ord('s'))

print(chr(115))

res = []

for x in 'spam':
    res.append(ord(x))      # Manual results collection

print(res)

res = list(map(ord, 'spam'))        # Apply function to sequence (or other)
print(res)

res = [ord(x) for x in 'spam']      # Apply expression to sequence (or other)
print(res)

print([x ** 2 for x in range(10)])

print(list(map((lambda x: x ** 2), range(10))))