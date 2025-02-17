class Lunch:
    def __init__(self):                     # Make/embed Customer, Employee
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):              # Start a Customer order simulation
        self.customer.placeOrder(foodName, self.employee)

    def result(self):                       # Ask the Customer what Food it has
        self.customer.printFood()

class Customer:
    def __init__(self):                     # Initialize my food to None
        self.food = None

    def placeOrder(self, foodName, employee):   # Place order with an Employee
        self.food = employee.takeOrder(foodName)

    def printFood(self):                    # Print the name of my food
        print(self.food.name)

class Employee:
    def takeOrder(self, foodName):          # Return a Food, with requested name
        return Food(foodName)

class Food:
    def __init__(self, name):               # Store food name
        self.name = name

if __name__ == '__main__':
    x = Lunch()
    x.order('burritos')
    x.result()
    x.order('pizza')
    x.result()
