class NextClass:                        # Define class
    def printer(self, text):            # Define method
        self.message = text             # Change instance
        print(self.message)             # Access instance

x = NextClass()                         # Make instance

x.printer('instance call')              # Call its method

print(x.message)                        # Instance changed

NextClass.printer(x, 'class call')      # Direct class call

print(x.message)