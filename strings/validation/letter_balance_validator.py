text = input()
accents = "áéíóúÁÉÍÓÚ"

# Control variables
hasLowercase = False
hasAccent = False
hasSpace = False
countT = 0
countC = 0
countS = 0

for char in text:
    if char.islower():
        hasLowercase = True
        break
    if char in accents:
        hasAccent = True
        break
    if char == " ":
        hasSpace = True
        break
    if char == "T":
        countT += 1
    elif char == "C":
        countC += 1
    elif char == "S":
        countS += 1

if len(text) <= 10000 and not hasLowercase and not hasAccent and not hasSpace:
    if countT == countC and countC == countS and countT == countS:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
