class Ave:
    def __init__(self):
        self.flyer = True
    
    def fly(self):
        print("The bird is flying.")

class Duck(Ave):
    def __init__(self):
        super().__init__() # Initialize the parent class
        self.swimmer = True

    def fly(self):
        super().fly()
        print("The duck is flying.")

duck = Duck()
duck.fly()  # Output: The bird is flying. The duck is flying.

print(duck.flyer, duck.swimmer)  # Output: True True