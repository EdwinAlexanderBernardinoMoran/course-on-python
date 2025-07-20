class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} has been deleted.")

    def __str__(self):
        return f"Class Dog: {self.name}, Age: {self.age}"

    def speak(self):
        print(f"{self.name} says Woof!")


dogOne = Dog("Buddy", 3)
print(dogOne)  # This will print the object representation}

del dogOne  # This will trigger the __del__ method
