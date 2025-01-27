name = 'Bob Smith'          # Simple string, outside class

print(name.split())         # Extract last name

print(name.split()[-1])     # Or [1], if always just two parts

pay = 100000                # Simple variable, outside class

pay *= 1.10                 # Give a 10% raise

print('%.2f' % pay)         # Or: pay = pay * 1.10, if you like to type
                            # Or: pay = pay + (pay * .10), if you _really_ do!

# Process embedded built-in types: strings, mutability

class Person:
    def __init__(self, name,  job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])         # Extract object's last name
    sue.pay *= 1.10                     # Give this object a raise
    print('%.2f' % sue.pay)
