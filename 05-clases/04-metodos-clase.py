class Dog: # PascalCase / UpperCamelCase
    paws = 4  # Class property (attribute)

    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    @classmethod
    def speak(cls):
        print(" says Woof!")

    @classmethod
    def factory(cls):
        return cls("Default Name", 0)

Dog.speak()  # Calling the class method
dog = Dog("Buddy", 3)
dogTwo = Dog("Max", 5)
dogThree = Dog.factory()  # Using the factory method

print(f"{dogThree.name} is {dogThree.age} years old and has {dogThree.paws} paws.")