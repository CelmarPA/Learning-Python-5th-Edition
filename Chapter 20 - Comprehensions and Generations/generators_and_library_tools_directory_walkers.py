import os

for (root, subs, files) in os.walk('.'):        # Directory walk generator
    for  name in files:
        if name.startswith('generators'):
            print(root, name)