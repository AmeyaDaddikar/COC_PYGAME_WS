from itertools import cycle
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

def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')

    while True:
        IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
	IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[0]).convert(),
            pygame.image.load(PLAYERS_LIST[1]).convert(),
            pygame.image.load(PLAYERS_LIST[2]).convert(),
        )
        
    	if 'win' in sys.platform:
       		soundExt = '.wav'
    	else:
        	soundExt = '.ogg'
        SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)
        mainGame()

def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerAccY    =   1   # players downward accleration
    playerFlapAcc =  -9   # players speed on flapping
    loopIter      =   0
    playerIndex   =   0

    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerFlapAcc #accelerate karvao
                SOUNDS['wing'].play()
        
        playerVelY += playerAccY
        playery += playerVelY
	
	#in simple terms, player wing flap karane 
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerFlap)
        loopIter = (loopIter + 1) % 30 #har 30 frames me flap

        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerIndex], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
