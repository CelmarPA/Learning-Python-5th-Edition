# Find the largest Python source file in a single directory

import os, glob

dirName = r'C:\Python312\Lib'

allSizes = []

allPy = glob.glob(dirName + os.sep + '*.py')

for fileName in allPy:
    fileSize = os.path.getsize(fileName)
    allSizes.append((fileSize, fileName))

allSizes.sort()
print(allSizes[:2])
print(allSizes[-2:])
