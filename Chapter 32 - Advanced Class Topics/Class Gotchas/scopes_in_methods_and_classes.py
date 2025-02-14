def generate():
    class Spam:                         # Spam is a name in generate's local scope
        count = 1
        def method(self):
            print(Spam.count)           # Visible in generate's scope, per LEGB rule (E)
    return Spam()

def generate():
    return Spam()

class Spam:                             # Define at top level of module
    count = 1
    def method(self):
        print(Spam.count)               # Works: in global (enclosing module)

generate().method()

def generate(label):                    # Returns a class instead of an instance
    class Spam:
        count = 1
        def method(self):
            print("%s=%s" % (label, Spam.count))

    return Spam

aclass = generate('Gotchas')

I = aclass()

I.method()
