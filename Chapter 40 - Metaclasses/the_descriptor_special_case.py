from xxsubtype import spamdict


class C: pass                           # Inheritance special case #1...

I = C()                                 # Class data descriptors have precedence

print(I.__class__, I.__dict__)

I.__dict__['name'] = 'Bob'                      # Dynamic data in the instance
I.__dict__['__class__)'] = 'spam'               # Assign keys, not attributes
I.__dict__['__dict__'] = {}

print(I.name)                                   # I.name comes from I.__dict__ as usual
                                                # But I.__class__ and I.__dict__ do not!

print(I.__class__, I.__dict__)

class D:
    def __get__(self, instance, owner): print('__get__')
    def __set__(self, instance, value): print('__set__')

class C: d = D()                                # Data descriptor attribute

I = C()

I.d                                             # Inherited data descriptor access

I.d = 1

I.__dict__['d'] = 'spam'                        # Define same name in instance namespace dict

I.d                                             # But doesn't hide data descriptor in class!

class D:
    def __get__(self, instance, owner): print('__get__')

class C: d= D()

I = C()

I.d                                             # Inherited nondata descriptor access

I.__dict__['d']= 'spam'                         # Hides class names per normal inheritance rules

print(I.d)