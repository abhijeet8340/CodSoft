
num1 = int(input("Enter your First Number :: "))
num2 = int(input("Enter yor Second NUmber :: "))

print(" Press 1 for Addition \n Press 2 for Subtract \n Press 3 for Multiplication \n Press 4 for Division")

Choice = int(input("Enter your Choice 1 to 4: "))

if Choice == 1:
    print(num1, "+", num2, "The Addition of two Number is =", num1+num2)
elif Choice == 2:
    print(num1, "-", num2, " The Subtract of two Number is = ", num1-num2)
elif Choice == 3:
    print(num1, "x", num2,  "The Multiply of two Number is =", num1*num2)
elif Choice == 4:
    print(num1, "/", num2,  "The Division of two Number is =", num1/num2)
else:
    print("Please,Press Valid Number")



