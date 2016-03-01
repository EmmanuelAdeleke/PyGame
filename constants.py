score = 0
from random import *
# CONSTANT VARIABLES

# SCREEN DIMENSIONS
SCREEN_WIDTH  = 400 # X
SCREEN_HEIGHT = 600 # Y

# WINDOW TITLE (CHANGE ON DIFFERENT GAME STATES)
"""
1 - Display GAME_TITLE_1 on splash screen (startup)
2 - Display GAME_TITLE_2 to display the instructions and commands
3 - Display GAME_TITLE_3 when playing the game
4 - Display GAME_TITLE_4 when the game is over
"""
GAME_TITLE_1 = "Runner \"KING\" Jones (V1.04)"
GAME_TITLE_2 = "Runner \"KING\" Jones (V1.04) - Instructions" 
GAME_TITLE_3 = "Runner - Playing... (V1.04)"
GAME_TITLE_4 = "GAME OVER"

# COLOURS
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN   = (49,   139,   87) #46-139-87

# FRAME RATE PER SECONDS
FPS = 30

# AMOUNT OF AIR LEFT
air_left = 10
roundLeft = round(air_left, 5)
scoreLeft = round(score, 3)

WAITING_TIME = 0.000005

#PLAYER STARTS WITH INITIAL VALUE OF 0
PLAYER_SCORE = 0

# Player speed (pixels per frame)
PLAYER_SPEED = 20

# OBJECT SPAWN RATE
SPAWN_RATE = 2
FORCE_SPAWN = 3
ROCK_SPEED_LIMIT = 45

