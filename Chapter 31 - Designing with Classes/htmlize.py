from converters import Uppercase

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

Uppercase(open('trispam.txt'), HTMLize()).process()
