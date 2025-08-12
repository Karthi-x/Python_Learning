def calculate_love_score(name1,name2):

    list1=list("".join(name1.split())+"".join(name2.split()))
    checklist1=['t', 'r', 'u', 'e']
    checklist2=['l', 'o', 'v', 'e']

    Truepoint=0
    Lovepoint=0
    for i in list1:
        for x in checklist1:
            if i==x:
                Truepoint+=1

    for i in list1:
        for x in checklist2:
            if i==x:
                Lovepoint+=1




    print((Truepoint*10)+Lovepoint)

print("Lets check ypur love score")
name1=input("Whats your name:")
name2=input("Whats your partner's name:")

calculate_love_score(name1,name2)
