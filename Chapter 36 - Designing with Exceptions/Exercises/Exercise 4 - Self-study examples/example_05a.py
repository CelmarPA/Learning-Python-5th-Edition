# Similar to example_04, but using lists instead of dictionaries for sums

import sys

fileName = sys.argv[1]
numCols = int(sys.argv[2])
totals = [0] * numCols

for line in open(fileName):
    cols = line.split(',')
    nums = [int(x) for x in cols]
    totals = [(x + y) for (x, y) in zip(totals, nums)]

print(totals)

# execute command line: python example_05.py data.txt 3