class AgeDesc(object):
    def __get__(self, instance,  owner): return 40
    def __set__(self, instance, value): instance._age = value

class Descriptors(object):
    age = AgeDesc()

x = Descriptors()

print(x.age)                                                # Runs AgeDesc.__get__

x.age = 42                                                  # Runs AgeDesc.__set__

print(x._age)                                               # Normal fetch: no AgeDesc call
