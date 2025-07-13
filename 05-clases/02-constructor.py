class Dog: # PascalCase / UpperCamelCase

    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")
    
dog = Dog("Fido", 2)
dogTwo = Dog("Rex", 3)
print(dog.name)
dog.speak()

print(dogTwo.name)
dogTwo.speak()