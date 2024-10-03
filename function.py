# Der Benutzer wird dazu aufgefordert zwei Zahlen einzugeben. So bald beide Zahlen eingegeben sind, wird von beiden Zahlen das jeweilige Quadrat genommen und anschließend beide Zahlen in der Summe ausgerechnet.

while 1 == 1:
    print("Was möchten Sie tun?")
    print("1. Zwei Zahlen zum Quadrat in der Summe berechnen")
    print("2. Das Programm beenden")
    print("")

    choice = int(input("Bitte entscheiden Sie sich mit 1 oder 2: "))

    if choice == 1:
        print("Sie werden gleich aufgefordert zwei Zahlen einzugeben. Beide Zahlen werden im Quadrat genommen und dann zur Summe zu einander berechnet. Das Ergebnis wird Ihnen dann ausgegeben.")
        print("-----")
        numberOne = int(input("Bitte geben Sie die erste Zahl ein: "))
        numberTwo = int(input("Bitte geben Sie die zweite Zahl ein: "))
        print("-----")
        print("")
        def sum_of_squares(x, y):
            math1 = x ** 2
            print(f"Die erste Zahl zum Quadrat ist: {math1}")
            print("")
            math2 = y ** 2
            print(f"Die zweite Zahl zum Quadrat ist: {math2}")
            print("")
            finalMath = math1 + math2
            print(f"Die Summe beider Quadrate lautet also: {x}^2 + {y}^2 = {math1} + {math2} = {finalMath}")
        sum_of_squares(numberOne, numberTwo)
    elif choice == 2:
        print("Das Programm wird beendet. Auf Wiedersehen!")
        break
    else:
        print("Bitte geben Sie nur 1 oder 2 ein.")