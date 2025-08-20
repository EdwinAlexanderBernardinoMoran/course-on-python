from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def save(self):
        pass

class User(Model):
    def save(self):
        print("guardando en BBDD")

class Sesion(Model):
    def save(self):
        print("guardando en archivo")

def save(entities):
    # entity.save()

    for entity in entities:
        entity.save()

user = User()
session = Sesion()

save([user, session])