l = [1, 2, 3, 4, 5]
sm = 0

while l:
    sm += l[0]
    l = l[1:]

print(sm)

l = [1, 2, 3, 4, 5]
sm = 0

for x in l: sm += x

print(sm)