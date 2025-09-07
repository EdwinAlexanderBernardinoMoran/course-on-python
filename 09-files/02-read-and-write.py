from pathlib import Path

file = Path("09-files/test-file.txt")
text = file.read_text()
textTwo = file.read_text("utf-8").split("\n")

# Podemos modificar y trabajar con el listado que ya tenemos.
textTwo.insert(0, "New line added")

file.write_text("\n".join(textTwo), "utf-8")
print(text)
print(textTwo)