# from user_taxes import save, payTaxes = Importacion de modulos.
# from users.actions.utilities import save, payTaxes # Importacion de modulos que se encuentran dentro de paquetes
from users.taxes.utilities import payTaxes
import users

# print(dir(users))
# print(users.__name__)
# print(users.__package__)
# print(users.__path__)
# print(users.__file__)

# save()
payTaxes()