# Similar to example_04, but using lists instead of dictionaries for sums


fileName = 'data.txt'

with open(fileName, 'r') as file:
    numCols = len(file.readline().split(','))

totals = [0] * numCols

for line in open(fileName):
    cols = line.split(',')
    nums = [int(x) for x in cols]
    totals = [(x + y) for (x, y) in zip(totals, nums)]

print(totals)
