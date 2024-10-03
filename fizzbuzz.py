# Dies ist ein Programm das die Zahlen von 1 bis 100 durchläuft. Diese werden geprüft ob sie durch 3 oder 5 teilbar sind. Es gibt sogar aus ob die Zahl durch 3 und 5 Teilbar ist und die Zahl selbst ausgibt wenn sie durch keine der beiden teilbar ist.

x = 0

while x <= 100:
    math = (x % 3)
    math2 = (x % 5)
    math3 = (math == 0) and (math2 == 0)
    if math3 == 1:
        print("Fizzbuzz")
        x += 1
    elif math == 1:
        print("Fizz")
        x += 1
    elif math2 == 1:
        print("Buzz")
        x += 1
    else:
        print(x)
        x += 1