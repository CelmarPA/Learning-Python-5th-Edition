import simple       # First import: loads and runs file's code

print(simple.spam)      # Assignment makes an attribute

simple.spam = 2         # Change attribute in module

import simple       # Just fetches already loaded module

print(simple.spam)      # Code wasn't rerun: attribute unchanged
