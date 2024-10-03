# Der Benutzer soll eine Eingabe vollführen. Es soll geprüft werden ob die Eingabe eine Zahl ist und wenn ja, ob sie positiv oder negativ oder null ist

userInput = int(input("Bitte geben sei eine Zahl ein: "))
typeCheck = isinstance(userInput, int)
if typeCheck == 1:
    if userInput == 0:
        print("Die Zahl ist Null.")
    elif userInput >= 1:
        print("Die Zahl ist Positiv.")
    elif userInput <= -1:
        print("Die Zahl ist Negativ")
else:
    print("Die Eingabe ist keine Zahl.")