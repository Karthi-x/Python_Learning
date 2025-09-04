alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(input_data,encryption_value):
    val=[]    # the output is an empty list
    # for each value in the input 
    for i in input_data:
            a=25 # no of alphabets
            for l in alphabets:
                if i != l:
                    a=a-1
            if a==-1: # looked throu all the alphabets and didnt find a match, means its not in the alphabet
                 msg_index=i
                 val.append(msg_index) #appending, joining the value to the list
            else:
                # letter to be changed(msg_index) is position in alphabet[] plus+ enval
                msg_index=alphabets.index(i)+encryption_value # increasing the alphabet by the enceyp value
                # joining it to th eprevious value
                val.append(alphabets[msg_index])

    print(f"Your Encrypted value is \n{(''.join(val))}")
    print(f"Your Shift number is {encryption_value}\n")

def decryption(input_data,decryption_value):
    val=[]    
    # for each value in the input 
    for i in input_data: 
            a=25
            for l in alphabets:
                    if i != l:
                        a=a-1
            if a==-1:
                msg_index=i
                val.append(msg_index)
            else: 

                # letter to be changed(msg_index) is position in alphabet[] plus+ enval
                msg_index=alphabets.index(i)-decryption_value
                # joining it to th eprevious value
                val.append(alphabets[msg_index])
    print(f"Your Decrypted value is \n{(''.join(val))}\n")

continuee=True
while continuee:
     

    input_of_user=input("Press 'E' for encrypting\nPress 'D' for Decrypting\n: ")

    if input_of_user.lower() =="e":
        input_data=input("Enter the message to be encypted :\n ").lower()
        encryption_value=int(input("Enter the encryption value:\n "))
        encryption(input_data,encryption_value)
    elif input_of_user.lower() == "d" :
        input_data=input("Enter the message to be decypted :\n ").lower()
        decryption_value=int(input("Enter the decryption value:\n "))
        decryption(input_data,decryption_value)
    else:
        print("Wrong value Press E or D")
        continue

    conti=input("Do you want to continue?\nY or y for yes and N or n for NO ").lower()
    if conti=="y":
        continuee = True # if true the program will run again
    elif conti=="n":
        continuee = False # if false it will stop
        print("Ok Byee")
    else:
        print("Type Y or N stupid")
        continuee = True
