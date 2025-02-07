from listtree import ListTree
from tkinter import Button                      # Both classes have a __str_

class MyButton(ListTree, Button): pass          # ListTree first: use its __str__

B = MyButton(text = 'spam')

print(open('savetree.txt', 'w').write(str(B)))       # Save to a file for later viewing

print(len(open('savetree.txt').readlines()))         # Lines in the file

print(B)                                             # Print the display here

S = str(B)                                           # Or print just the first part

print(S[:1000])
