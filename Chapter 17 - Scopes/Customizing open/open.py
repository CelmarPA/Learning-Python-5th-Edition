F = open('script2.py')      # Call built-in open in builtins
print(F.read())

from makeopen import makeopen       # Import open resetter function

makeopen('spam')        # Custom open calls built-in open
File = open('script2.py')       # Call custom open in builtins
print(File.read())

makeopen('eggs')        # Nested customizers work too!
File2 = open('script2.py')      # Because each retains own state
print(File2.read())