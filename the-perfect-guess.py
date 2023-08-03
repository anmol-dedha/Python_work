import random
randam_num=random.randint(1,100)
# print(randam_num)
guesses=0

user_number=None # it's important to define the user_number before going into while loop

while user_number!=randam_num:
    user_number=int(input('Guess the Number : '))

    if user_number>randam_num:
        print('Guess a Lower Number')
        
    elif user_number<randam_num:
        print('Guess a Higher Number')
        
    elif user_number==randam_num:
        print('Congratulations You guess the right number')
        
    elif user_number>100:
        print('Please select number between 1 to 100')
    
    guesses+=1
    

print(f'total attempt to guess the right number is {guesses}')

with open('02_project_The_Perfect_Guess\his_her_score.txt','r')as f:
    his_her_score=int(f.read())

if (guesses<his_her_score):
    print("you score high score!")
    with open("02_project_The_Perfect_Guess\his_her_score.txt",'w') as f :
        f.write(str(guesses))




