from turtle import Screen
import pygame
import random
import math
from pygame import mixer

#initializing pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("SpaceInvadersGame\icons\space-ship.png")
pygame.display.set_icon(icon)

#background Image
background_img = pygame.image.load("SpaceInvadersGame\icons\Backgroung_image.jpg")


#Background Music
mixer.music.load('SpaceInvadersGame\sounds\Background.wav')
mixer.music.play(-1)







#Adding Images to the Game
#Initializing player image
player_img = pygame.image.load("SpaceInvadersGame\icons\spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0


def player(x, y):#function to add player image
    screen.blit(player_img, (x, y))#Adds an image to the screen


#Initializing bullet Image
bullet_img = pygame.image.load("SpaceInvadersGame\icons\Bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 2
bullet_state = "ready"#ready means bullet is not visible




#Updating Score function
score_value = 0#initializing Score Variable
text_x = 10
text_y = 10
font = pygame.font.Font('freesansbold.ttf', 32)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


#Showing Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (320, 290))


#Initializing Multiple Enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 8
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("SpaceInvadersGame\icons\space-ship.png")) 
    enemy_x.append(random.randint(0,736)) #Randomly adds the enemy in any place b/w 0 and 800
    enemy_y.append(random.randint(30, 150)) 
    enemy_x_change.append(0.3) 
    enemy_y_change.append(30)

    
         


def enemy(x, y, i ):#function to add enemy image
    screen.blit(enemy_img[i], (x, y))#Adds an image to the screen

#Firing Function
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

#COLLUSION DETECTION
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 30:
        return True
    else:
        return False




 
#GAME LOOP
running = True
while running:
    screen.fill((0,0,0)) #adding color to screen
    
    #Adding Background
    screen.blit(background_img, (0,0))
    
    #quitting Game
    for event in pygame.event.get():#goes through all the events
        if event.type == pygame.QUIT:#if close button is pressed
            running = False

    #Adding Keyboard functions
    #if KeyStrokes is pressed check ehether its right or left
        if event.type == pygame.KEYDOWN: #if any key is Pressed
            
            if event.key == pygame.K_LEFT:
                player_x_change -= 0.3
            if event.key == pygame.K_RIGHT:
                player_x_change += 0.3
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('SpaceInvadersGame\sounds\laser.wav')
                bullet_sound.play()
                bullet_x = player_x#stores current position of that space ship so when we fire bullet comes there
                fire_bullet(bullet_x, bullet_y)
                
        #Releasing our hands off the keys
        if event.type == pygame.KEYUP: #If we release the key and the key comes to its normal form
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0#stops when we take our hands of the arrow key
               
        

    player_x += player_x_change#Adding the changes to the original

    #Adding Boundries so that our spaceship won't go outside of it
    if player_x <= 0:#0 is starting point of x-axis
        player_x = 0
    if player_x >= 736: #800-64(800 is screen width and image is 64x64 px so substract 64)
        player_x = 736

    #Making Multiple Enemy Spaceship to move continously and also adding boundaries
    for i in range(num_of_enemies):
        #Game Over function
        if enemy_y[i] > 460:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()


        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:#0 is starting point of x-axis
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736: #800-64(800 is screen width and image is 64x64 px so substract 64)
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i]
        
        #COLLUSIONS
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            explosion_sound = mixer.Sound('SpaceInvadersGame\sounds\explosion.wav')
            explosion_sound.play()
            bullet_y = 480#brings bullet back to its starting point
            bullet_state = "ready"
            score_value += 1#updates the score
            
            
            #chooses random place for enemy
            enemy_x[i] = random.randint(0,736)
            enemy_y[i] = random.randint(30, 150)
        
        #respawns enemies at random place
        enemy(enemy_x[i], enemy_y[i], i)


    #Shooting Multiple bullets(Not muliple bullets its actually same bullet multiple times)
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    #bullet Movement
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

        
    player(player_x, player_y) #adding player so it must be visible throughout the game
    show_score(text_x, text_y)
    pygame.display.update()#updates the screen every time we add something new



