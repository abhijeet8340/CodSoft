import random
Character = "ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&"


while True:
    length_pass = int(input("Enter your length of password :: "))
    count_pass = int(input("Enter your count of password :: "))
    for i in range(0, count_pass):
        password = ""
        for j in range(0, length_pass):
            count_pass = random.choice(Character)
            password = password+count_pass
        print("The generated password is ", password)
    repeat = input("Generate More Password ?")
    if repeat == "no" or repeat == "NO":
        break

print("Thank you!!!")


