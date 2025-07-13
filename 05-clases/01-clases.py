class Dog: # PascalCase / UpperCamelCase
    def speak(self):
        print("Woof!")
    
dog = Dog()
dog.speak()  # Output: "Woof!"

print(isinstance(dog, Dog))  # Output: True