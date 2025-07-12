import random

list_of_words=["apple", "giraffe", "mountain", "computer", "jazz", "whistle", "oxygen", "banana", "pyramid", "galaxy", "rhythm", "keyboard", "castle", "island", "voyage", "dragon", "submarine", "nugget", "pirate", "desert"]

word            =random.choice(list_of_words)
blanks =list("_" * len(word))
# OR  LIKE BELOW
#length_of_word  =len(word)
#blank           ="_" * length_of_word
#blanks          =list(blank)

lives           =5
letters_of_word =list(word)



print(word) # For Testing
# all the \n are for a better visual, else all would look crammed
print(f"\n{blanks}")
print(f"\n    You have {lives} lives\n")



while not lives==0 and not letters_of_word==blanks:
    gussed_letter=input("  Guess a Letter :")
    print("\n")
    n=0
    letter_present=False
    for i in letters_of_word:
        if i==gussed_letter:
            blanks[n]=i
            letter_present=True
        n=n+1
    print(f"-----------------------\n \n    You have {lives} lives\n")
    print(f"\n{blanks}\n")
    if letter_present==False:
        lives=lives-1
    else:
        print(f"    {gussed_letter} is in the word\n")
    print(f"    You have {lives} lives\n")
    


if lives==0:
    print(f"    You have Lost the game\n")
    print(f"    The word was {word}\n")
else:
    print(f"    You have WON the game!!!!\n-----------------------")
