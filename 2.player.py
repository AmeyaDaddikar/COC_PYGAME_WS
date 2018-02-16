from itertools import cycle
import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
"""
Create a tuple PLAYER_LIST
HAVING THE ADDRESS OF 3 BIRD FLAPPING POSTION IN THE ORDER (UP,MID,DOWN)

PLAYERS_LIST = (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png')
"""
#YOUR CODE
IMAGE={}
"""
CREATE AN EMPTY DICTIONARY NAMED SOUNDS FOR ADDING FLAPPING SOUNDS
 SOUNDS =  {}
"""
#YOUR CODE
def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    """
    IN THE IMAGES DICTIONARY
    LOAD 3 FLAPPING IMAGES OF BIRD
    STORED IN THE TUPLE PLAYER_LIST USING ALPHA CHANNEL HAVING 'player' AS THE KEY
    IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[2]).convert_alpha(),
        )
    """
    

    """
    Sound extension selection based on windows and ubuntu
    Add wing sound into the SOUNDS dictionary with key 'wing'
    if 'win' in sys.platform:
       	soundExt = '.wav'
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)
    """
    while True:
        mainGame()

def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    gravity    =   1   # players downward accleration
    playerUp =  -9   # players speed on flapping
    loopIter      =   0
    playerWingPos   =   0

    while True:
        
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            """
            INSIDE THIS FOR LOOP
            CHECK IF SPACEBAR OR THE UP KEY IS PRESSED
            IF PRESSED SET THE PLAYERS VERTICAL VELOCITY AND SHOULD PLAY THE BIRD FLAPPING SOUND 
            
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerUp #accelerate karvao
                SOUNDS['wing'].play()
            """
        """
        OUTSIDE THE EVENT LOOP
        UPDATE THE PLAYER'S VERTICAL VELOCIY BY ADDING GRAVITY
        NOW UPDATE THE PLAYER'S ACTUAL Y COORDINATE USING PLAYER'S VERTICAL VELOCITY
        
        playerVelY += gravity
        playery += playerVelY
	"""

	
        """
        DECIDING WHICH PLAYER IMAGE TO DRAW ON SCREEN UP FLAP/MID FLAP/DOWN FLAP 
        USING THE loopIter VARIABLE
        CHANGE THE playerWingPos ACCORDINGLY(0 OR 1 OR 2)
        
        if (loopIter + 1) % 3 == 0:
            playerWingPos = next(playerFlap)
        loopIter = (loopIter + 1) % 30 
        """
        SCREEN.blit(IMAGES['background'], (0,0))
        """
        DRAW THE SELECTED PLAYER IMAGE ON THE SCREEN AT THE COORDINATE player,playery
    
	SCREEN.blit(IMAGES['player'][playerWingPos], (playerx, playery))
        """
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
