#!python

from __future__ import print_function
from commuter import Commuter1, Commuter2, Commuter3, Commuter4, Commuter5

if __name__ == '__main__':
    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
        print('-' * 60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)
