

import random

user=input("choose R or P or S\n")

if user=="r":
    user="Rocks"
elif user=="p":
    user="Papers"
elif user=="s":
    user="Scissors"

compuer_choise=["Rocks","Papers","Scissors"]
ran=random.randint(0,2)

com=compuer_choise[ran]

print (f"You choose     {user}")
print(f"Computer choose {com}\n")



if com=="Rocks" and user=="Rocks" :
    print( '''
    _______                         _______
---'   ____)                       (____    '---
      (_____)                    (_____)
      (_____)                    (_____)
      (____)                      (____)
---.__(___)                        (___)__.---
          
    ROCKS                           ROCKS
'''
)
    print ("draw")

elif com=="Scissors" and user=="Scissors":
    print('''
    _______                               _______
---'   ____)______                 ______(____   '---
          ________)               (________
       __________)                 (__________
      (____)                           (____)
---.__(___)                             (___)__.---
          
    SCISSORS                            SCISSORS

          ''')
    print ("draw")

elif com=="Papers" and user=="Papers":
    print( ''''
     _______                                 _______
---'    ____)______                  ______(____    '---
           ________)              __(______
          _________)             (__________
         _________)               (__________          
---.____________)                   (________________.-
          
          PAPER                         PAPER
          ''')
    print ("draw")




elif com=="Rocks" and user=="Papers":
    print( '''
    _______                          _______
---'   ____)                ________(____   '---
    __(_____)              (________
      (______)            (__________
      (_____)              (_________
---.__(____)                 (_____________.-----

     ROCK                          PAPER

          ''')
    print ("You Won")

elif com=="Scissors" and user=="Rocks":
    print( '''
    _______                          _______
---'   ____)______                  (____   '---
          ________)               (_____)
         __________)              (_____)
        (____)                    (____)
---.__(___)                        (___)__.---

    SCISSORS                          ROCK
          ''')
    print ("You Won")

elif com=="Papers" and user=="Scissors":
    print( '''
    _______                                _______
---'   ____)______                _______(____   '---
          ________)              (_________
          __________)            (__________
          _________)                   (____)
---._____________)                       (___)__.---

     PAPER                         SCISSORS
          ''')
    print ("You Won")



elif com=="Rocks" and user=="Scissors":
    print( '''
    _______                           _______
---'   ____)__                _______(____   '---
        (_____)              (________
        (______)            (__________
        (_____)                   (____)
---.____(____)                     (___)__.---
          
         ROCKS                       SCISSORS
          ''')
    print ("You Lost")

elif com=="Scissors" and user=="Papers":
    print( '''
    _______                                _______
---'   ____)______                _______(____   '---
          ________)              (_________
         __________)            (__________
        (____)                   (_________
---.____(___)                       (____________.---

    SCISSORS                          PAPER
          ''')
    print ("You Lost")

elif com=="Papers" and user=="Rocks":
    print( '''
   _______                             _______
---'   ____)______                    (____   '---
          ________)                (____)
         ___________)              (____)
        ___________)                (____)
---.______________)                  (___)__.---
          
     PAPER                             ROCK
          ''')
    print ("You Lost")

else:
    print ("You Lostfewfefwfr")
