class Attrs:
    def __getattr__(self, name):
        print('get %s' % name)

    def __setattr__(self, name, value):
        print('set %s %s' % (name, value))

x = Attrs()

x.append

x.spam = 'pork'
