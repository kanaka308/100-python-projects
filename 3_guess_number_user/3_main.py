import random

computer_guess = random.randint(1,100)
user_guess = None


guess = 0

while(user_guess != computer_guess):
    
    user_guess = int(input('Guess the number: '))
    if user_guess < computer_guess:
        print("bigger")
    elif user_guess > computer_guess:
        print("smaller")
    guess += 1

    
print(f"You guessed it right in {guess} guesses")
with open("3_guess_number_user/highscore.txt", 'r') as f:
    highscors = f.read()

if int(guess) < int(highscors):
    print("You broke the highscore")
    with open("3_guess_number_user/highscore.txt", 'w') as f:
        f.write(str(guess))
    
    
    
