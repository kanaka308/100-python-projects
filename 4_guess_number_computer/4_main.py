import random

start = 1
end = 100

user_choice = int(input("Choose a number: "))
computer_choice = None
feedback = None
guess = 0
print('''choose:
     'h' if number is higher
     'l' if number is lower
     'c' if the number is correct''')


while(user_choice != computer_choice):
    
    computer_choice = random.randint(start, end)
    print(computer_choice)
    

    
    if(start != end):
        feedback = input("Give Feedback: ")

        if feedback == 'h':
            start = computer_choice + 1
        elif feedback == 'l':
            end = computer_choice -1
        elif feedback == 'c':
            print("correct")
            
    guess += 1
print(f"the computer guessed in {guess} guesses")



    