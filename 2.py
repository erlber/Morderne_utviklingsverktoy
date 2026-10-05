print("Velkommen til kalkulatoren")

tall1 = input("Tall 1: ")
tall2 = input("Tall 2: ")

valg = input("Velg +, -, * eller /: ")

if valg == "+":
    svar = tall1 + tall2

elif valg == "-":
    svar = tall1 - tall2

elif valg == "*":
    svar = tall1 * tall2

elif valg == "/":
    svar = tall1 / tall2

print("Svaret er", svar)