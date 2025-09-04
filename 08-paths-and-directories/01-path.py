from pathlib import Path

# window = Path(r"C:\Users\Edwin\Documents\course-on-python\08-paths-and-directories")
# linux = Path("/home/edwin/course-on-python/08-paths-and-directories")

# path_absolute = Path("/home/edwin/course-on-python/08-paths-and-directories")
# path_relative = Path("08-paths-and-directories/")

path = Path("08-paths-and-directories/my_file.txt")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)