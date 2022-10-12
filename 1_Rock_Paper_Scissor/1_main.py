import random

def Rock_Paper_Scissor(user, computer):
    
    if user == computer:
        print("it's a Draw")
        

    if user == "r":
        if computer == "s":
            
            return True
            
            
        elif computer == "p":
            
            return False
            

    if user == "p":
        if computer == "s":
            
            return False
            

        elif computer == "r":
            
            return True
            

    if user == "s":
        if computer == "p":
            
            return False
        

            
        elif computer == "r":
            
            return True
            
    
print('''choose:
r - Rock
p - paper
s - scissor''')

rounds = int(input("Enter how many Ronuds you want to play: "))
user_wins = 0
computer_wins = 0
draws = 0


for i in range(1, rounds+1):


    user_choice = input("Make you choice: ")
    rn = random.randint(1,3)
    computer_choice = -1
    
    if rn == 1:
            computer_choice = "r"
            
    elif rn == 2:
            computer_choice = "p"
        
    elif rn == 3:
            computer_choice = "s"
            

    print(f'you choose {user_choice}')
    print(f'the computer chose {computer_choice}')
    winner = Rock_Paper_Scissor(user_choice, computer_choice)
    if winner == True:
        print('=============You won============')
        user_wins += 1
    elif winner == False:
        print('=============you lost!===========')
        computer_wins += 1
    else:
        draws += 1
    print(f"round {i} complete")
    print("*************************************************************************************")

    

    
print(f'round - {rounds}')
print(f'user wins - {user_wins}')
print(f'computer wins - {computer_wins}')
print(f"draws - {draws}")

if user_wins > computer_wins:
    print('**********************You are the winner*************************')
elif user_wins < computer_wins:
    print('**********************You are the looser*************************')
else:
    print('***********************its a overall draw*************************')
    
    



    


    




    
            