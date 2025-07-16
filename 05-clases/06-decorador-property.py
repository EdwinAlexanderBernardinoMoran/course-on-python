class Dog:

    def __init__(self, name):
        self.name = name

    @property # Solo se utiliza con las funciones que devuelven un valor en este caso las properties
    def name(self):
        print("Getting name...")
        return self.__name

    @name.setter
    def name(self, name):
        print("Setting name...")
        if name.strip():
            self.__name = name
        return


dogOne = Dog("Buddy")
print(dogOne)
print(dogOne.name)  # Accessing the private attribute through a method