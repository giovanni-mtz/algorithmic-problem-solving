name = input()
accents = "áéíóúÁÉÍÓÚ"

valid = True

for char in name:
    if char in accents or char == " ":
        valid = False
        break

if valid and len(name) <= 10:
    print(f"Hello {name}!")
