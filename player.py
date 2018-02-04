from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *


FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
PLAYERS_LIST = (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png')
IMAGES, SOUNDS = {}, {}


try:
    xrange
except NameError:
    xrange = range


def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')

    while True:
        # select random background sprites
        IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
	IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[2]).convert_alpha(),
        )
        
        # sounds
    	if 'win' in sys.platform:
       		soundExt = '.wav'
    	else:
        	soundExt = '.ogg'
        
        SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)
	movementInfo = {
                    'playery': SCREENHEIGHT/2,
                    'playerFlap': cycle([0, 1, 2, 1]),
                }
        mainGame(movementInfo)

def mainGame(movementInfo):
    playerFlap = movementInfo['playerFlap']
    playerx, playery = int(SCREENWIDTH * 0.2), movementInfo['playery']
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerAccY    =   1   # players downward accleration
    playerFlapAcc =  -9   # players speed on flapping
    loopIter      =   0
    playerIndex   =   0

    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(1)
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerFlapAcc #accelerate karvao
                SOUNDS['wing'].play()
        playerVelY += playerAccY
        playery += playerVelY
	
	#in simple terms, player wing flap karane 
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerFlap)
        loopIter = (loopIter + 1) % 30

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerIndex], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
