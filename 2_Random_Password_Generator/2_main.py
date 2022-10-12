#Input the Length of the password
#choose the type of password pin(numbers), passcode(numbers and alphabets(all small)) and tough password(alphabets(smallcase,uppercase), numbers and symbols)
#Generate the password
#Print The Password

import random
from secrets import choice
import string

all_characters_for_pin = string.digits
all_characters_for_weak_password = list(string.ascii_lowercase + string.digits)
all_characters_for_medium_password = list(string.ascii_letters + string.digits)
all_characters_for_strong_password = list(string.ascii_letters + string.digits + '!@#$%^&*()-+=/.,|')


def password_generator(length, type):
    password = []
    if type == "pin":
        for i in range(length):
            password.append(random.choice(all_characters_for_pin))
        password = "".join(password)
        print(password)
        

    elif type == "weak":
        for i in range(length):
            password.append(random.choice(all_characters_for_weak_password))
        password = "".join(password)
        print(password)
        

    elif type == "medium":
        for i in range(length):
            password.append(random.choice(all_characters_for_medium_password))
        password = "".join(password)
        print(password)
        

    elif type == "strong":
        for i in range(length):
            password.append(random.choice(all_characters_for_strong_password))
        password = "".join(password)
        print(password)

    else:
        print("invalied type")

   

        
            




print('''Choose the type of password:
"pin" to generate a pin, 
"weak" to generate a weak password and
"strong" to generate a strong password''')
type = input("Enter the type of password: ")
length = int(input("Enter the length: "))


password_generator(length, type)