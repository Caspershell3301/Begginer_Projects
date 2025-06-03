def add(a, b):
   res = a + b
   print(str(a) + "+" + str(b) + "=" + str(res) + "\n")

def subt(a, b):
    res = a - b
    print(str(a) + "-" + str(b) + "=" + str(res) + "\n")

def mult(a, b):
    res = a * b
    print(str(a) + "X" + str(b) + "=" + str(res) + "\n")

def divi(a, b):
    res = a / b
    print(str(a) + "/" + str(b) + "=" + str(res) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit" + "\n")

    choice = input("Enter your Choice : ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("your first number: "))
        b = int(input("second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Your first number: "))
        b = int(input("second number: "))
        subt(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Your first number: "))
        b = int(input("second number: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Your first number: "))
        b = int(input("second number: "))
        divi(a, b)
    elif choice == "e" or choice == "E":
        print("Thank You for the visit. Ending the Program!!")
        quit()




