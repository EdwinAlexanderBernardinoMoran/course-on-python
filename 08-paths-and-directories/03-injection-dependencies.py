class Database:
    def save(self, entity):
        print(f"Saving {entity} to the database")

class Entity:
    def __init__(self, name):
        self.name = name

    def save(self):
        print(f"Entity {self.name} saved")

def save_with_dependency(entity, repository):
    repository.save(entity)

# Ejemplo de uso:
db = Database()
entity = Entity("Test")
save_with_dependency(entity, db)