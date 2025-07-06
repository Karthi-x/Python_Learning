# password generator

import random

# List all letters, nums and symbols
alpha  =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nums   =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", "\"", ",", ".", "/",  "<", ">", "?", "~", "`"]

passlength=int(input("What is the lenght of the password you want? ")) #gets the length of the password requires

# numbers and symbols required in the password should not be more than the length of the password
# making sure the num length and symbol length is lower
while True:
    numlength = int(input(f"Out of {passlength} How many numbers should be there? "))
    if numlength > passlength:
        print("Numbers exceed length of the password. Please try again.")
    else:
        break  

while True:
    passlength = passlength-numlength
    symbolslength=int(input(f"Out of {passlength} How many symbols should be there? "))
    if symbolslength > passlength:
        print("Numbers exceed length of the password. Please try again.")
    else:
        break  

alphalength=passlength-symbolslength

# generating random letters
password=""
for x in range(0,alphalength):
    a=random.choice(alpha)
    password=password+a

# generating random numbers
for x in range(0,numlength):
    a=random.choice(nums)
    password=password+a

# generating random symbols
for x in range(0,symbolslength):
    a=random.choice(symbols)
    password=password+a

password_list=list(password)

# shuffeling the password
random.shuffle(password_list)
Final_password=""
for i in password_list:
    Final_password=Final_password+i

print(f"Password is: {Final_password}")
