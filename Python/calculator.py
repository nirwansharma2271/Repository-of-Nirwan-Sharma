print("Welcome to Python calculator!")
a = input("Do you want to continue? (Enter Y/N):")
if a == "Y":
    print("Code for different operators:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for modulus\n6 for exponentiation\n")
    code = int(input("Enter the code:"))
    if code == 1:
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("result is", a + b)  
    elif code == 2:
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("result is", a - b)  
    elif code == 3:
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("result is", a * b) 
    elif code == 4:
        a = float(input("Enter the dividend:"))
        b = float(input("Enter the divisor:"))
        if b != 0:
            print("result is", a / b)  
        else:
            print("Divisor cannot be 0")
    elif code == 5:
        a = float(input("Enter the dividend:"))
        b = float(input("Enter the divisor:"))
        if b != 0:
            print("result is", a % b) 
        else:
            print("Divisor cannot be 0")
    elif code == 6:
        a = float(input("Enter the base:"))
        b = float(input("Enter the exponent:"))
        print("result is", a ** b)  
    else:
        print("No such code")
else:
    print("Exited the calculator.")
