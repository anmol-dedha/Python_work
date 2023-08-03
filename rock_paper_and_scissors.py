
computer=print("computer has enterd his turn !")
user_=(input("Enter You Turn: "))

import random
comp_turn=random.randint(1,3) # here the 1 means rock , 2 means paper and 3 means scissor

if comp_turn==1:
    if user_=="r":
        print("it's a Draw ,both of you draw a Rock")
    elif user_=="p":
        print("You won , you beat computer's rock by your paper")
    elif user_=="s":
        print("you lost, You draw scissor against computer's rock")

elif comp_turn==2:
    if user_=="p":
        print("it's a Draw ,both of you draw a Paper")
    elif user_=="s":
        print("You won , you beat computer's paper by your scissor")
    elif user_=="r":
        print("you lost, You draw Rock against computer's paper")

elif comp_turn==3:
    if user_=="s":
        print("it's a Draw ,both of you draw a scissor")
    elif user_=="r":
        print("You won , you beat computer's scissor by your Rock")
    elif user_=="p":
        print("you lost, You draw Paper against computer's scissor")

# print(comp_turn)
# print(user_)
