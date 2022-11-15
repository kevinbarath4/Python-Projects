
unum1 = float(input("Please Enter a First Number: "))
uope1 = input("Please Enter an Operator (+ - / * %): ")
unum2 = float(input("Please Enter a Second Number: "))

if uope1 == "+":
    print(float (unum1) + float (unum2))

elif uope1 == "-":
    print(float (unum1) - float (unum2))

elif uope1 == "/":
    print(float (unum1) / float (unum2))

elif uope1 == "%":
     print(float (unum1) % float (unum2))

elif uope1 == "*":
    print(float (unum1) * float (unum2))

else:
    print ("Please Restart Program, Issue with entered variables or operator")