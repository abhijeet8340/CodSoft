print("-------------> Contact Book <<------------")
Name = []
Contact_number = []
Email = []
Addres = []
num = 2

for i in range(num):
    Names = input("Name :: ")
    Contact_numbers = int(input("Contact Number :: "))
    Emails = input("Enter Email :: ")
    Address = input("Enter Address :: ")
    Name.append(Names)
    Contact_number.append(Contact_numbers)
    Email.append(Emails)
    Addres.append(Address)

print("\tName\t\t\tContact_number\t\t\tEmail\t\t\tAddress")

for i in range(num):
    print(f'\t{Name[i]}\t\t\t{Contact_number[i]}\t\t\t{Email[i]}\t\t\t{Addres[i]}')

s = input("Enter the name to serach :: ")
if s in Name:
    index = Name.index(s)
    Names = Name[index]
    Contact_numbers = Contact_number[index]
    Emails = Email[index]
    Address = Addres[index]

    print(f"Name ::{Names} , Contact Number ::{Contact_numbers} , Email ::{Emails} , Address ::{Address}")
else:
    print("Name is not found")




