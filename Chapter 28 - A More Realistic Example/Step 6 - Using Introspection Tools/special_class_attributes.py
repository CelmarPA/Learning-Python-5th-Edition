from person import Person

bob = Person('Bob Smith')

print(bob)                      # Show bob's __repr__ (not __str__)

print(bob.__class__)            # Show bob's class and its name

print(bob.__class__.__name__)

print(list(bob.__dict__.keys()))            # Attributes are really dict keys
                                            # Use a list to force a list in 3.X

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])     # Index manuall

for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))     # obj.attr, but attr is a var