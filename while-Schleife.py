# Das Programm erfordert eine Nutzereingabe, diese soll geprüft werden ob die Zahl Gerade oder Ungerade ist. So lange sie ungerade ist, soll das Programm weiter laufen

x = 1

while x == 1:
    print("Bitte geben sie gleich eine Zahl ein. So lange diese Zahl ungerade ist, werden sie immer wieder zu einer neuen Eingabe aufgefordert. So bald sie gerade ist, beendet sich das Programm.")
    userInput = int(input("Bitte geben Sie eine Zahl ein: "))
    if (userInput % 2) == 1:
        x == 1
    elif (userInput % 2) == 0:
        x = 0
        print(f"Die Zahl {userInput} ist gerade.")
    