# Find the largest Python source file on the module import search path

import sys, os, pprint

visited = {}
allSizes = []

for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        thisDir = os.path.normpath(thisDir)
        if thisDir.upper() in visited:
            continue
        else:
            visited[thisDir.upper()] = True

        for fileName in filesHere:
            if fileName.endswith('.py'):
                pyPath = os.path.join(thisDir, fileName)

                try:
                    pySize = os.path.getsize(pyPath)
                except:
                    print('skipping', pyPath)

                allSizes.append((pySize, pyPath))

    allSizes.sort()
    pprint.pprint(allSizes[:3])
    pprint.pprint(allSizes[-3:])
