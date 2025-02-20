# Find the largest Python source file in an entire directory tree

import sys, os,  pprint

if sys.platform[:3] == 'win':
    dirName = r'C:\Python312\Lib'
else:
    dirName = '/usr/lib/python'

allSizes = []

for (thisDir, subsHere, filesHere) in os.walk(dirName):
    for fileName in filesHere:
        if fileName.endswith('.py'):
            fullName = os.path.join(thisDir, fileName)
            fullSize = os.path.getsize(fullName)
            allSizes.append((fullSize, fullName))

allSizes.sort()

pprint.pprint(allSizes[:2])
pprint.pprint(allSizes[-2:])
