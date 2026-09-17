print("Welcome to the Math Module! The currently available functions are: addition, subtraction, division, exponentiation, modulus, multiplication")


def addition():
    print("Enter 2 numbers: ")
    x = input()
    y = input()
    print("The sum of " + x + " and " + y + " is " + str(int(x) + int(y)))


def subtraction():
    print("Enter 2 numbers: ")
    x = input()
    y = input()
    print("The difference of " + x + " and " + y + " is " + str(int(x) - int(y)))


def division():
    print("Enter 2 numbers: ")
    x = input()
    y = input()
    print("The quotient of " + x + " and " + y + " is " + str(int(x) / int(y)))


def exponentiation():
    print("Enter 2 numbers: ")
    x = input()
    y = input()
    print("The exponentiation of " + x + " and " + y + " is " + str(int(x) ** int(y)))


def modulus():
    print("Enter 2 numbers: ")
    x = input()
    y = input()
    print("The modulus of " + x + " and " + y + " is " + str(int(x) % int(y)))


def multiplication():
    print("Enter 2 numbers: ")
    x = input()
    y = input()
    print("The product of " + x + " and " + y + " is " + str(int(x) * int(y)))


choice = input("Please enter the function you would like to use: ")

switch = {
    "addition": addition,
    "subtraction": subtraction,
    "division": division,
    "exponentiation": exponentiation,
    "modulus": modulus,
    "multiplication": multiplication
}

switch[choice]()