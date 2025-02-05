class Wrapper:
    def __init__(self, object):
        self.wrapped = object                       # Save object

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)                 # Trace fetch
        return getattr(self.wrapped, attrname)      # Delegate fetch

x = Wrapper([1, 2, 3])                              # Wrap a list

x.append(4)                                         # Delegate to list method

print(x.wrapped)                                    # Print my member

x = Wrapper({'a': 1, 'b': 2})                       # Wrap a dictionary

print(list(x.keys()))                               # Delegate to dictionary method
