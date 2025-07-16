class Dog:

    def __init__(self, name, age = 0):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def speak(self):
        print(f"{self.__name} dice: ¡Guau!")

    @classmethod
    def factory(cls):
        return cls("Lobo", 0)
    
dogOne = Dog.factory()
dogOne.speak()  # Calling the instance method
print(dogOne.get_name())  # Accessing the private attribute through a method

# ESTO NO SE DEBE HACER SOLO ES DEMOSTRATIVO PARA ENTENDER EL CONCEPTO QUE SE PUEDE ACCEDER A LOS ATRIBUTOS PRIVADOS
print(dogOne.__dict__) # Accessing the instance's dictionary
print(dogOne._Dog__name)  # Accessing the private attribute directly (not recommended)

dogOne.set_name("Rocky")  # Changing the name using the setter method