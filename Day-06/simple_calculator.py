A = int(input("Enter Number For A: "))
B = int(input("Enter Number For B: "))

print("-------------------- Simple Calculator --------------------")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

option = int(input("Choose option 1 to 5: "))

match option:
    case 1:
        C = A + B
        print("A + B =", C)

    case 2:
        D = A - B
        print("A - B =", D)

    case 3:
        E = A * B
        print("A * B =", E)

    case 4:
        F = A // B
        print("A // B =", F)

    case 5:
        G = A % B
        print("A % B =", G)

    case _:
        print("Invalid Input")
