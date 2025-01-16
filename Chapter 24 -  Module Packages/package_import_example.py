import dir1.dir2.mod        # First imports run init files

import dir1.dir2.mod        # Later imports do not


from importlib import reload

reload(dir1)

reload(dir1.dir2)

print(dir1)

print(dir1.dir2)

print(dir1.dir2.mod)

print(dir1.x)

print(dir1.dir2.y)

print(dir1.dir2.mod.z)
