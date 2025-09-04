from pathlib import Path

path = Path("rutas")
# path.mkdir()
# path.rmdir()
# path.rename("new_directory")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("new_directory")

for p in path.iterdir():
    print(p)