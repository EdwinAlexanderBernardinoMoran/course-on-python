from pathlib import Path
from time import ctime

file = Path("09-files/test-file.txt")
# file.exists()
# file.rename()
# file.unlink()

print(file.stat()) # Para poder ver la información del archivo ejecuta python 09-files/01-file.py en la terminal
print("Acceso", ctime(file.stat().st_atime))
print("Creacion", ctime(file.stat().st_ctime))
print("Modificacion", ctime(file.stat().st_mtime))