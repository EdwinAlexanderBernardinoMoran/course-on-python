class Dog: # PascalCase / UpperCamelCase
    paws = 4  # Class property (attribute)

    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woof!")
    
dog = Dog("Fido", 2)
dogTwo = Dog("Rex", 3)

print(Dog.paws)  # Accessing class property
Dog.paws = 3  # Modifying class property

dog.paws = 5  # Modifying instance property
print(dog.paws)  # Accessing modified instance property
print(dogTwo.paws)  # Accessing class property from instance

print(dogTwo.name)
dogTwo.speak()