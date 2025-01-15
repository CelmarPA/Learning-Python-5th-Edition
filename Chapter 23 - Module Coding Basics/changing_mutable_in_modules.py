from small import x, y      # Copy two names out

x = 42          # Changes local x only

y[0] = 42       # Changes shared mutable in place

import small        # Get module name (from doesn't)

print(small.x)      # Small's x is not my x
print(small.y)      # But we share a changed mutable
