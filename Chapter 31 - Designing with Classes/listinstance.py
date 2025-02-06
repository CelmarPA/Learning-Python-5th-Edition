#!python

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; displays instances attrs only; self is
    instance of the lowest class; __X names avoid clashing with client's attrs.
    """
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    """def __atranames(self):
        return ''.join('\t%s=%s\n' % (attr, self.__dict__[attr])
                        for attr in sorted(self.__dict__))"""

    def __str__(self):
        return '<Instance of %s, adress %s:\n%s>' %(
                            self.__class__.__name__,            # My class's name
                            id(self),                           # My address
                            self.__attrnames())                 # name=value list

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)

