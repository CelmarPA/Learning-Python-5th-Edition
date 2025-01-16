from dir1.dir2 import mod       # Code path here only

print(mod.z)        # Don't repeat a path

from dir1.dir2.mod import z

print(z)

import dir1.dir2.mod as mod          # Use shorter name

print(mod.z)

from dir1.dir2.mod import z as modz         # Ditto if names clash

print(modz)
