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
        # background sprites
        IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    	# numbers sprites for score display
    	IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
        )        

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
        SOUNDS['point']   = pygame.mixer.Sound('assets/audio/point' + soundExt)
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
    score         =   0
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

	# check for score
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
		print score
                SOUNDS['point'].play()
	
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
        showScore(score)
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
    
def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][digit].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) /2

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][digit].get_width()


if __name__ == '__main__':
    main()
