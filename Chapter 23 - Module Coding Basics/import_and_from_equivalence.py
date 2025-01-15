from module import name1, name2         # Copy these two names out (only)

import module       # Fetch the module object

name1 = module.name1        # Copy names out by assignment

name2 = module.name2

del module      # Get rid of the module name

print(name1)
print(name2)