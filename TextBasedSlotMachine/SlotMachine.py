import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { #there are 4 symbols each symbol is repeated the value times
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values = { #values of each symbol 
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):#to check if the user got 3 same symbols in one column
    winnings = 0 #total money won(initially zero)
    winning_lines = [] #the line which got 3 same symbols
    for line in range(lines):#lines which user gave us
        symbol = columns[0][line]#this is the starting columns symbol
        for column in columns:
            symbol_to_check = column[line] #other 2 columns containg symbols
            if symbol != symbol_to_check: #checking if the symbol of starting columns symbol is equal to symbols of other 2 columns
                break
        
        else:
            winnings += values[symbol] * bet #refering to symbol_values
            winning_lines.append(line + 1)
    
    return winnings, winning_lines





     

def get_slot_machine_spin(rows, cols, symbols):#randomly spins the slot mahine
    all_symbols = []
    for symbol, symbol_count in symbols.items():#iterating over a dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] #all columns
    for col in range(cols):
        column = [] #each colum
        current_symbols = all_symbols[:] #Actually copying elements of all symbols to current symbols so if we change current symbol all_aymbols won't be affected
        
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns



def print_slot_machine(columns):
    #transposing the matrix as columns are in rows form
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): 
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")


        print()

# Taking a Deposit Amount from the users
def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit? : $")
        if amount.isdigit():
            amount = int(amount) #converting input sring to integer
            if amount > 0: #amount must be greater than 0
                break
            else:
                print("Amount Must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


#taking number of lines from the users 
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a number between (1-"+str(MAX_LINES)+")" )
        else:
            print("Enter a valied number")
    
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on Each line ? : $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter an amount between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a valid amount that is a nmuber")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet, your current balance is: ${balance}")
        else:
            break
         
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won {winnings}")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

    
            
        

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer =  input("Press enter to play(q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

     
main()







