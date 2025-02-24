# Sum columns in a text file separated by commas

fileName = 'data.txt'

sums = {}

for line in open(fileName):
    cols = line.split(',')
    nums = [int(col) for col in cols]
    for (ix, num) in enumerate(nums):
        sums[ix] = sums.get(ix, 0) + num
for key in sorted(sums):
    print(key, '=', sums[key])
