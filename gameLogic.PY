import pygame, os, sys # IMPORT PYGAME, SYS, OS
from pygame.locals import * # IMPORT ALL THE CONTENTS FROM THE PYGAME LOCALS
from constants import * #constants.py (in folder)
from random import * # IMPORT ALL THE CONTENTS FROM THE RANDOM MODULE
from time import * # IMPORT ALL THE CONTENTS FROM THE TIME MODULE

pygame.init() # INITIALIZE PYGAME
pygame.mixer.init() # INITIALIZE PYGAME'S MIXER
fpsClock = pygame.time.Clock() #FPSCLOCK WILL BE USED TO SLOW DOWN OUR PYGAME

# SURFACE OBJECT: CREATE SURFACE OBJECT FOR OBJECTS TO BE DISPLAYED   
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
ROCK_SPEED = 20
# CAPTION (SPLASH SCREEN)
pygame.display.set_caption(GAME_TITLE_1) # DISPLAY THE CAPTION
splash = pygame.image.load('.\images\splash_screen.jpg') # LOAD THE SPLASH IMAGE FROM THE SPLASH FOLDER
screen.blit(splash, (0, 0)) # BLIT THE IMAGE ONTO THE SCREEN AT (0, 0)

# MOVING BACKGROUND
bround = ".\images\\background.jpg" # ASSIGN THE STRING TO BROUND
br = pygame.image.load(bround).convert_alpha() # LOAD THE BACKGROUND IMAGE FROM THE IMAGES FOLDER
br2 = pygame.image.load(bround).convert_alpha() # LOAD THE BACKGROUND IMAGE AGAIN
y = 0 # ASSIGN 0 TO THE Y VARIABLE. WILL BE USED FOR THE MOVING BACKGROUND

# LOADING THE PLAYER SPRITE
player = pygame.sprite.Sprite()
player.image = pygame.image.load('.\images\walk1.gif').convert_alpha() 
player.rect = player.image.get_rect()
player_group = pygame.sprite.GroupSingle(player)
player.rect.left = (SCREEN_WIDTH / 2) - 1 #STARTING POSITION OF PLAYER (Y)
player.rect.bottom = SCREEN_HEIGHT - 10 # STARTING POSITION OF PLAYER (Y)

# LOADING THE ROCKS / ENEMY SPRITE
"""
rock = pygame.sprite.Sprite()
rock.image = pygame.image.load('.\images\\rock.png').convert_alpha() 
rock.rect = rock.image.get_rect()
rock_group = pygame.sprite.GroupSingle(rock)
rock.rect.left = (SCREEN_WIDTH / 2) - 1
rock.rect.bottom = 20
"""

# STORES A LIST OF ALL THE ROCKS
rock_list = pygame.sprite.OrderedUpdates()

# STORES A LIST OF ALL THE ROCKS
air_list = pygame.sprite.OrderedUpdates()

velocity_x = 0
velocity_y = 0

            # MUSIC / SOUND

# LOAD THE INTRO MUSIC FROM THE MUSIC FOLDER
music = pygame.mixer.Sound('.\sounds\jayz_holy_grail_intro3.wav')
# LOAD THE MAIN MUSIC FROM THE MUSIC FOLDER
music2 = pygame.mixer.Sound('.\sounds\jayz_holy_grail_main3.wav')
# LOAD THE POWERUP FROM THE MUSIC FOLDER
pwrup = pygame.mixer.Sound('.\sounds\powerup.wav') 

music.play(-1) # LOOP MUSIC (INTRO) CONTINUOUSLY

def quit(): # QUIT FUNCTION
    pygame.quit() # CLOSES PYGAME (SETS ALL VALUES TO HALT)
    sys.exit() # ALLOWS THE WINDOW TO BE CLOSED

def instructions(): # INSTRUCTION FUNCTION
    pygame.display.set_caption(GAME_TITLE_2) # SET THE CAPTION TO DIFFERENT STATE
    instructions = pygame.image.load('.\images\instruction_screen.jpg') # LOAD THE INSTRUCTION SCREEN
    screen.blit(instructions, (0, 0)) # BLIT THE INSTRUCTIONS ONTO THE SCREEN

def game(): # GAME FUNCTION
    global validOption # GET VALIDOPTION (GLOBAL FUNCTION)
    pygame.display.set_caption(GAME_TITLE_3) # SET THE CAPTION TO DIFFERENT STATE
    screen.fill(BLACK) # FILL THE SCREEN WITH A BLACK COLOUR
    music.stop() # STOP THE MUSIC PLAYING (INTRO)
    music2.stop() 
    music2.play(-1) # LOOP CONTINUOUSLY
    validOption = 1 * - 1 # MULTIPLY 1 BY -1

def lose2(): # LOSE 2 FUNCTION
    global scoreLeft # GET SCORELEFT (GLOBAL FUNCTION)
    pygame.display.set_caption(GAME_TITLE_3) # SET THE CAPTION TO DIFFERENT STATE
    lose2 = pygame.image.load('.\images\lose2.jpg') # LOAD LOSE2.JPG IMAGE FROM THE IMAGES FOLDER
    screen.blit(lose2, (0, 0)) # BLIT THE LOSE2.JPG TO SCREEN
    screen.blit(final_score, (240, 240)) # BLIT THE VALUE OF THE SCORE AT (240, 240)
    screen.blit(final_score_label, (20, 240)) # BLIT THE LABEL AT (20, 240)

def lose1(): # LOSE 1 FUNCTION
    global scoreLeft # GET THE GLOBAL VARIABLE SCORELEFT
    pygame.display.set_caption(GAME_TITLE_3) # SET THE CAPTION TO DIFFERENT STATE
    lose1 = pygame.image.load('.\images\lose1.jpg') # LOAD LOSE2.JPG IMAGE FROM THE IMAGES FOLDER
    screen.blit(lose1, (0, 0)) # BLIT THE LOSE1.JPG TO SCREEN
    screen.blit(final_score, (240, 240)) # BLIT THE VALUE OF THE SCORE AT (240, 240)
    screen.blit(final_score_label, (20, 240)) # BLIT THE LABEL AT (20, 240)
    

rock = pygame.sprite.Sprite()
rock.image = pygame.image.load('.\images\\rock.png').convert_alpha()
rock.rect = rock.image.get_rect()

air = pygame.sprite.Sprite()
air.image = pygame.image.load('.\images\\powerup.png').convert_alpha()
air.rect = air.image.get_rect()

color = GREEN # ASSIGN COLOR TO THE CONSTANT VALUE GREEN
color2 = BLACK # ASSIGN COLOR2 TO THE CONSTANT VALUE BLACK 
score = 0

def addRock(rock_list):
    # CREATE A SPRITE FOR THE POWER UP CALLED ROCK
    global rock, velocity_y
    rock = pygame.sprite.Sprite()

    # LOAD THE IMAGE ROCK IN THE IMAGES FOLDER
    rock.image = pygame.image.load('.\images\\rock.png').convert_alpha()

    # GET THE RECTANGLE / POINTS OF THE ROCK
    rock.rect = rock.image.get_rect()

    # POSITIONING OF THE ROCK
    rock.rect.left = randint(20, SCREEN_WIDTH - 30)
    
    #rock.rect.top = velocity_y 
    rock_list.add(rock)
    #pygame.time.set_timer(pygame.USEREVENT, 1000)

def addAir(air_list):
    # CREATE A SPRITE FOR THE POWER UP CALLED AIR
    global air, velocity_y
    air = pygame.sprite.Sprite()

    # LOAD THE IMAGE POWERUP IN THE IMAGES FOLDER
    air.image = pygame.image.load('.\images\\powerup.png').convert_alpha()

    # GET THE RECTANGLE / POINTS OF THE POWERUP
    air.rect = air.image.get_rect()

    # POSITIONING OF THE POWERUP
    air.rect.left = randint(0, SCREEN_WIDTH - 17)
    air.rect.top = velocity_y + 5
    air_list.add(air) # ADD TO THE AIR_LIST (KEEPS TRACK OF AIR_LIST)

    """ WAS USED TO DETERMINE HOW OFTEN A POWERUP WILL FALL
    BETWEEN THE VALUES 10000 (10 SECONDS) AND 30000 (30 SECONDS)
    HOWEVER, THERE WAS TROUBLE AS A ROCK WOULD NOT FALL TILL
    THE TIME PASSES SO I COULD NOT USED USEREVENT, RATE.
    rate = randint(10000, 30000)
    #pygame.time.set_timer(pygame.USEREVENT, RATE)
    #print(rate)
    """
    
ticktock = 1
validOption = 1
rock.rect.top = 0

while True: # THE MAIN GAME LOOP
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
        # QUIT BUTTON OR ESCAPE BUTTON OR THE LETTER Q TO TERMINATE THE GAME
        # (GOTO QUIT() FUNCTION AND EXECUTE pygame.quit() and sys.exit())
            quit()
        
        # IF THE USER PRESSES KEY DOWN
        if event.type == KEYDOWN:
        
            # CHECK IF "I" IS PRESSED AND validOptionvalid --> 1
            # (GOTO INSTRUCTIONS(), CHANGE THE CAPTION AND LOAD IMAGE AND BLIT TO SCREEN)
            if event.key == K_i and validOption == 1:
                validOption = 1
                instructions()
            
            # CHECK IF "ENTER" IS PRESSED AND validOption --> 1
            # (GOTO GAME(), CHANGE THE CAPTION AND FILL THE SCREEN WITH BLACK)
            if event.key == K_RETURN and validOption == 1:
                if validOption == 1:
                    validOption = validOption * - 1
                    game()
                
        #if event.type == pygame.USEREVENT:
            #addRock(rock_list)
            #addAir((air_list))

        # IF THE USER PRESSES KEY DOWN
        if event.type == pygame.KEYDOWN: # IF THE KEYDOWN IS PRESSES
            
            if event.key == K_RIGHT: # IF THE RIGHT KEY IS PRESSED
                velocity_x += PLAYER_SPEED # VELOCITY_X += PLAYER_SPEED (20)
            if event.key == K_LEFT: # IF THE LEFT KEY IS PRESSED
                velocity_x -= PLAYER_SPEED # VELOCITY_X -= PLAYER_SPEED (20)
                
        elif event.type == KEYUP: # DETECT WHEN KEYUP IS PRESSED
            if event.key == K_RIGHT: 
                velocity_x -= PLAYER_SPEED
            elif event.key == K_LEFT:
                velocity_x += PLAYER_SPEED

    # ENSURE THAT THE USER CANNOT GO OFF THE SCREEN
    # IF THE PLAYER'S RECT RIGHT POSITION IS MORE THAN THE SCREEN_WIDTH (400)
    if player.rect.right + velocity_x > SCREEN_WIDTH: 
        player.rect.right = SCREEN_WIDTH # THEIR POSITION WILL EQUAL SCREEN_WIDTH
                                         # CANNOT GO RIGHT OF THE SCREEN ANYMORE
    elif player.rect.left + velocity_x < 0: # IF THE LEFT POSITION IS LESS THAN 0
        player.rect.left = 0 # THEIR POSITION WILL EQUAL 0 (CANNOT GO LEFT OF THE SCREEN)
    else: # ELSE: THE RECT OF THE PLAYER WILL BE INCREMENTED BY VELOCITY_X
        player.rect.x += velocity_x

    if validOption == -1:
        # MOVING BACKGROUND
        screen.blit(br, (0, y)) # BLIT BR AT (0, Y)
        screen.blit(br2,(0, y - SCREEN_HEIGHT)) # BLIT BR AT (0, Y - SCREEN_WIDTH)
        """
        BOTH IMAGES ARE BLIT ONTO THE SCREEN. ONE AT (0, 0)
            WHERE X WILL REMAIN 0 AND Y WILL BE INCREMEMNTED BY 4
        THE OTHER IMAGE WILL BE BLIT AT (0, 0 - SCREEN_HEIGHT)
            WHERE THE SCREEN_HEIGHT WILL BE INCREMENRED BY 4 LATER

        AS THE LOOP GOES ON THE IMAGE WILL APPEAR TO BE MOVING AS THE IMAGE GOES
        OFF THE SCREEN ANOTHER IMAGE WILL APPEAR ON SCREEN, CREATING THE
        ILLUSION THAT THE BACKGROUND IS MOVING.
        """
        y = y + 4 # (GOES UP IN MUTLIPLES OF 4)

        # IF THE Y VALUE IS EQUAL TO 400 THEN RESET THE VALUE OF Y
        if y == 600:
            y = 0
        # DETECT COLLISION BETWEEN THE PLAYER AND THE THE ROCK
        # IF THE THEY DO COLLIDE THEN THE PLAYER SHOULD BE REMOVED
        pygame.sprite.groupcollide(player_group, rock_list, True, False)

        # DETECT COLLISION BETWEEN THE PLAYER AND THE THE POWER-UP
        # IF THE THEY DO COLLIDE THEN THE POWER-UP SHOULD BE REMOVED
        pygame.sprite.groupcollide(player_group, air_list, False, True)
        
        #screen.fill(BLACK) # FILL THE SCREEN WITH THE COLOUR BLACK (NOT USED)    
        player_group.draw(screen) # DRAW THE SPRITE ON THE SCREEN

        rock_list.draw(screen) # DRAW THE ROCK AFTER PLAYER

        air_list.draw(screen) # DRAW THE POWERUP AFTER ROCK

        # HANDLES THE ROCK SPEED
        rock.rect.top += 10 # INCREMENT THE SPEED OF THE ROCK BY +10
        if scoreLeft >= 10: # IF THE SCORE IS MORE THAN OR EQUAL TO 10
            rock.rect.top += 5 # INCREASE THE SPEED OF THE ROCK BY += 5
            air.rect.top += 3 # INCREASE THE SPEED OF THE POWER-UP BY += 3
        if scoreLeft >= 45: # IF THE SCORE IS MORE THAN OR EQUAL TO 45
            rock.rect.top += 5 # INCREASE THE SPEED OF THE ROCK BY += 5
            air.rect.top += 3 # INCREASE THE SPEED OF THE POWER-UP BY += 3
        if scoreLeft >= 70: # IF THE SCORE IS MORE THAN OR EQUAL TO 70
            rock.rect.top += 5 # INCREASE THE SPEED OF THE ROCK BY += 5
            air.rect.top += 3 # INCREASE THE SPEED OF THE POWER-UP BY += 3
        if scoreLeft >= 100: # IF THE SCORE IS MORE THAN OR EQUAL TO 10
            rock.rect.top += 5 # INCREASE THE SPEED OF THE ROCK BY += 5
            air.rect.top += 3 # INCREASE THE SPEED OF THE POWER-UP BY += 3

        air.rect.top += 5 # STARTING SPEED OF THE POWERUP 

        # IF THE ROCK EXCEEDS 600 THEN REMOVE IT FROM THE SCREEN
        if rock.rect.top > 600:
            rock_list.remove(rock)

        # IF THE POWER-UP EXCEEDS 600 THEN REMOVE IT FROM THE SCREEN
        if air.rect.top > 600:
            air_list.remove(air)    

        # FORCE THE SPAWN OF A ROCK AND A POWERUP
        """ COULDNT SPAWN USING USEREVENT"""
        if FORCE_SPAWN % SPAWN_RATE == 1: # FORCE_SPAWN % SPAWN_RATE IS:
                                          # 3 % 2 = 1 THEN DO:
            if len(rock_list) < 3:        # IF THE LENGTH OF ROCK LIST IS LESS THAN 3
                addRock(rock_list)        # THEN PERFORM ADDROCK FUNCTION

        if FORCE_SPAWN % SPAWN_RATE == 1: # FORCE_SPAWN % SPAWN_RATE IS:
                                          # 3 % 2 = 1 THEN DO:
            if len(air_list) < 3:         # IF THE LENGTH OF ROCK LIST IS LESS THAN 3
                #addRock(rock_list)        # THEN PERFORM ADDROCK FUNCTION  
                addAir(air_list)

        sleep(WAITING_TIME) # INTERVAL AT 0.000005 (CONSTANT)
        air_left -= 0.009 # AFTER 0.000005 SECONDS DECREMENT BY 0.009 
        
        roundLeft = round(air_left, 3) # FORMAT AIR_LEFT TO 3.D.P AND ASSIGN TO ROUNDLEFT

        multiplier = randint(11, 19) / 10 # RANDOM NUMBER BETWEEN 10 AND 20 (NOT INCLUDING) 
        
        score += 0.009 * multiplier # SCORE ADD THE MULTIPLER
        scoreLeft = round(score, 2) # ROUND THE SCORE TO TWO DECIMAL PLACES FOR DISPLAY

        """ HANDLE THE PLAYER'S SCORE & AMOUNT OF AIR LEFT """
        # DRAW A WHITE RECTANGLE AT POINT (SCREEN_WIDTH (400), 45) AT THE VALUE (0, 0)
        pygame.draw.rect(screen, WHITE, (0,0,SCREEN_WIDTH,45), 0)

        # CREATES FONT OBJECT WITH SIZE 25
        # CREATE ANOTHER FONT OBJECT WITH SIZE 75
        my_font = pygame.font.Font(None, 25)
        final_font = pygame.font.Font(None, 75)

        # ALLOWS A TEXT TO BE DRAWN ONTO A SURFACE 
        air_left_show = my_font.render(str(roundLeft), 0, (color))
        screen.blit(air_left_show, (300, 12)) # BLIT THE AIR LEFT AT (300, 12)

        air_label = my_font.render(("AIR LEFT: "), 0, (color2))
        screen.blit(air_label, (215, 12)) # BLIT AIR_LABEL AT (215, 12)

        score_label = my_font.render(("SCORE: "), 0, (BLACK))
        screen.blit(score_label, (60, 12)) # BLIT THE BLACK SCORE_LABEL AT (60, 12)

        # CONVERT SCORELEFT TO A STRING (CAN ONLY BLIT STRINGS)
        score_left = my_font.render(str(scoreLeft), 0, (BLACK))
        screen.blit(score_left, (125, 12)) # BLIT THE BLACK VALUE / SCORE (125, 12)

        final_score = final_font.render(str(scoreLeft), 0, (WHITE))
        final_score_label = final_font.render(("SCORE: "), 0, (WHITE))

        if air_left <= 0: # IF THE AMOUNT OF AIR IS LESS THAN 0
            validOption = 1 # SET VALID OPTION TO 1
            screen.fill(BLACK) # FILL THE SCREEN WITH THE COLOUR BLACK
            lose1() # PERFORM THE LOSE1 FUNCTION
            air_left = 0 # SET AIR_LEFT TO 0
            score = 0 # SET SCORE TO 1

        if air_left <= 5: # IF THE AMOUNT OF AIR IS LESS THAN 5
            color = RED # SET THE VARIABLE COLOR TO RED. (CHANGED LABEL FROM GREEN TO BLACK)
            color2 = RED # SET THE VARIABLE COLOR TO RED. (CHANGES THE SCORE FROM GREEN TO BLACK)
        elif air_left >= 5: # ELSEIF AIR IS MORE THAN 5
            color = GREEN # CHANGE THE COLORS BACK TO GREEN 
            color2 = GREEN # CHANGE THE COLOR TO GREEN

        # CHECKS WHETHER THE PLAYER AND POWER-UP HIT / COLLIDE
        if pygame.sprite.collide_rect(player, air):
            score += 0.5 # WHEN DETECTION IS FOUND INCREMENT THE SCORE BY 0.5
            air_left += 1.2 # WHEN DETECTION IS FOUND INCREMENT THE AIR BY 1.2
            pwrup.play()
            
        # CHECKS WHETHER THE PLAYER AND POWER-UP HIT / COLLIDE
        if pygame.sprite.collide_rect(player, rock):
            validOption = 1 # CHANGE THE VALIDOPTION TO 1
            lose2() # PERFORM THE LOSE2 FUNCTION
            
    pygame.display.update()

    fpsClock.tick(FPS)
