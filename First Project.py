# Basic Aritmetic calculaor for two numbers WIP

def Addition(num1, num2):
    return int (num1) + int (num2)
def Subtraction(num1, num2):
    return int (num1) - int (num2)
def Multiplication(num1, num2):
    return int (num1) * int (num2)
def Divison(num1, num2):
    return float (num1) / float (num2)
def Mod(num1, num2):
    return float (num1) % float (num2)

unum1 = input("Please Enter a Number: ")
unum2 = input("Please Enter a Number: ")

Addition = Addition(unum1, unum2)
Subtraction = Subtraction(unum1, unum2)
Multiplication = Multiplication(unum1, unum2)
Division = Divison(unum1, unum2)
Mod = Mod(unum1, unum2)

print (str(Addition) + "\n" + str(Subtraction) + "\n" + str(Multiplication) + "\n" + str(Division) + "\n" + str(Mod))
