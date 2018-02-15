from itertools import cycle
import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
'''
### Create another global constant to store a tuple of string paths of the Red bird
PLAYERS_LIST = (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png')
### Create an empty dictionary variable to store SOUNDS
SOUNDS = {}
'''
IMAGES = {}
def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    '''
    ### Add the 3 converted images as a tuple to IMAGES with key 'player'
    IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[2]).convert_alpha(),
        )
    ### Sound extension selection based on windows and ubuntu
    if 'win' in sys.platform:
       	soundExt = '.wav'
    else:
        soundExt = '.ogg'
    ### Add wing sound into the SOUNDS dictionary with key 'wing'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)
    '''
    while True:
        mainGame()

def mainGame():

    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =  4   # player's velocity along Y, default same as playerFlapped
    gravity    =   1   # players downward accleration
    playerUp =  -9   # players speed on flapping
    loopIter      =   0
    playerWingPos   =   0

    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        ''''
        ### Key event to make bird jump using space or up keys. also play 'wing' sound
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerUp #accelerate karvao
                SOUNDS['wing'].play()
        ### Increase falling speed using gravity constant defined above
        playerVelY += gravity
        ### Change coordinate according to new speed
        playery += playerVelY

	#in simple terms, player wing flap karane 
        if (loopIter + 1) % 3 == 0:
            playerWingPos = next(playerFlap)
        loopIter = (loopIter + 1) % 30 #har 30 frames me flap
	'''
        SCREEN.blit(IMAGES['background'], (0,0))
        '''### Paint the bird image with appropriate wing position calculated above at player coordinates'''
	#######SCREEN.blit(IMAGES['player'][playerWingPos], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
