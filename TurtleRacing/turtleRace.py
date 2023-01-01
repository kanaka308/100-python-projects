import turtle
import random
import time

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'cyan', 'brown']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of Racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input a number bro!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Enter a number in between 2- 10 ')


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randint(1,20)
            racer.forward(distance)
        
        x, y = racer.pos()

        if y >= HEIGHT//2 - 20:
            return colors[turtles.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('TurtleRacing')


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
time.sleep(3)
print(f"the winner is color {winner}")
