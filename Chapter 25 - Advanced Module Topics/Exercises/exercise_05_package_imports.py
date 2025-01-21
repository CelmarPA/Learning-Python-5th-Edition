import mypkg.mymod

print(mypkg.mymod.countLines(r'mypkg\mymod.py'))

from mypkg.mymod import countChars

print(countChars(r'mypkg\mymod.py'))
