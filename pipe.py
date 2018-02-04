from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *


FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
BASEY        = SCREENHEIGHT * 0.79
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
Max_PipeY    =  220
Min_PipeY    =  100

PLAYERS_LIST = (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png')
PIPE = 'assets/sprites/pipe-green.png'
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
        IMAGES['pipe'] = (
            pygame.transform.rotate(
                pygame.image.load(PIPE).convert_alpha(), 180),
            pygame.image.load(PIPE).convert_alpha(),
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
    # get 2 new pipes to add to upperPipes lowerPipes list
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH , 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]

    # list of lowerpipe
    lowerPipes = [
        {'x': SCREENWIDTH , 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

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
        
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX
	
        # add new pipe when first pipe is about to touch left of screen
        if 0 <= upperPipes[0]['x'] <= 2:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])
	
        # remove first pipe if its out of the screen
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerIndex], (playerx, playery))
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def getRandomPipe():
    """returns a randomly generated pipe"""
    # y of gap between upper and lower pipe
    gapY = random.randrange(Min_PipeY, int(Max_PipeY)) #Range for bottom left most y coordinate of upper pipe 
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]

if __name__ == '__main__':
    main()
