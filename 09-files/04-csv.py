import csv
import os

# Escribir en un archivo CSV
# No es necesario cerrar el archivo
# with open("09-files/test-file.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "Test One"])
#     writer.writerow([1001, 2, "Test Two"])

# Leer un archivo CSV
# with open("09-files/test-file.csv", "r") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for line in reader:
#         print(line)


# Actualizar un archivo CSV
with open("09-files/test-file.csv") as r, open("09-files/test-file-temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for line in reader:
        if line[0] == "1000":
            writer.writerow([1000, 1, "Test One Updated"])
        else:
            writer.writerow(line)

    os.remove("09-files/test-file.csv")
    os.rename("09-files/test-file-temp.csv", "09-files/test-file.csv")