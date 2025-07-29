class Model():
    table = False

    def __nit__(self):
        if not self.table:
            print("No table defined for this model.")

    def save(self):
        print(f"Saving the model {self.table} to the database... ")
    
    @classmethod
    def filter_by_id(self, _id):
        print(f"Filtering by id {_id}...on table {self.table}")

class User(Model):
    table = "users"

user = User()
user.save()
User.filter_by_id(1)
