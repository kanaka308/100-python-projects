import curses
from curses import KEY_BACKSPACE, wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()#firstly clears the terminal
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to start")
    stdscr.refresh() #refreshes the terminal(i.e starts newly)
    stdscr.getkey()#allows user to type something befor refreshing


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2, 0, f"WPM: {wpm}")
    

    for i, char in enumerate(current):#displaying our current text over target text
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
        

def load_text():
    with open("randomtxt.txt", "r") as f:
        lines = f.readlines()
        line = random.choice(lines).strip()
        while "'" in line or "\"" in line or ":" in line or ";" in line or "-" in line:
            line = random.choice(lines).strip()
    return line


     
     

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    
    stdscr.nodelay(True)
   
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (time_elapsed/60) / 5)
        stdscr.clear()#clearing
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()#starts program freshly

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
            
        try: #to handle the above nodelay function
            key = stdscr.getkey()
        except:
            continue

        
        # if user presses backspace we must actually deleate the previous the letter
        if key in (KEY_BACKSPACE, '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)
        

        if ord(key) == 27: #27 is ASCII value of escape key
            exit()
        
        


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(3,0, "You completed the text! Press any key to continue")
        key = stdscr.getkey()
        
        
        if ord(key) == 27:
            exit()
        else:
            continue
            
        
wrapper(main)


  

 