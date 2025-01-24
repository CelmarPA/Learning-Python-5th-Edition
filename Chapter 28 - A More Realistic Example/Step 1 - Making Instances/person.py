class Person:
    def __init__(self, name, job = None, pay = 0):         # Constructor takes three arguments
        self.name = name                        # Fill out fields when created
        self.job = job                          # self is the new instance object
        self.pay = pay

if __name__ == '__main__':          # When run for testing only
    # Self-test code
    bob = Person('Bob Smith')           # Test the class
    sue = Person('Sue Jones', job = 'dev', pay = 100000)        # Runs __init__ automatically

    print(bob.name, bob.pay)                                                        # Fetch attached attributes
    print(sue.name, sue.pay)                                                        # sue's and bob's attrs differ