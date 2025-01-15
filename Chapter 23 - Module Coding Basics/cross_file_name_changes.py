from small import x, y      # Copy two names out

x = 42      # Changes my x only

print(x)

import small        # Get module name

small.x = 42        # Changes x in other modules

print(small.x)