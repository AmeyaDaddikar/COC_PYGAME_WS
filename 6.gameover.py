from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *


FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND   = 'assets/sprites/background-day.png'
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
Max_PipeY    =  220
Min_PipeY    =  100

PLAYERS_LIST = (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png')
PIPE = 'assets/sprites/pipe-green.png'
IMAGES, SOUNDS = {}, {}

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
        pygame.image.load('assets/sprites/0.png').convert(),
        pygame.image.load('assets/sprites/1.png').convert(),
        pygame.image.load('assets/sprites/2.png').convert(),
        pygame.image.load('assets/sprites/3.png').convert(),
        pygame.image.load('assets/sprites/4.png').convert(),
        pygame.image.load('assets/sprites/5.png').convert(),
        pygame.image.load('assets/sprites/6.png').convert(),
        pygame.image.load('assets/sprites/7.png').convert(),
        pygame.image.load('assets/sprites/8.png').convert(),
        pygame.image.load('assets/sprites/9.png').convert()
        )        

	IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[0]).convert(),
            pygame.image.load(PLAYERS_LIST[1]).convert(),
            pygame.image.load(PLAYERS_LIST[2]).convert(),
        )
        IMAGES['pipe'] = (
            pygame.transform.rotate(
                pygame.image.load(PIPE).convert(), 180),
            pygame.image.load(PIPE).convert(),
        )
        # sounds
    	if 'win' in sys.platform:
       		soundExt = '.wav'
    	else:
        	soundExt = '.ogg'
        
        SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)
        SOUNDS['point']   = pygame.mixer.Sound('assets/audio/point' + soundExt)
        SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt)
        SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)

        crashInfo = mainGame()
	showGameOverScreen(crashInfo)
	

def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
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
        {'x': newPipe1[0]['x'] , 'y': newPipe1[0]['y']},
        {'x': newPipe1[0]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ] #inital position of upper pipe

    # list of lowerpipe
    lowerPipes = [
        {'x': newPipe1[1]['x'] , 'y': newPipe1[1]['y']},
        {'x': newPipe1[1]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ] #inital position of lower pipe

    pipeVelX = -4

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

        # check for crash here
        crashTest = checkCrash({'x': playerx, 'y': playery, 'index': playerIndex},
                               upperPipes, lowerPipes)
        if crashTest[0]:
            return {
                'x': playerx,
                'y': playery,
                'groundCrash': crashTest[1],
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'score': score,
                'playerVelY': playerVelY,
                'playerVelY': playerAccY
            }

	# check for score
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 3:
                score += 1
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
    scoreDigits = list(str(score))
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][int(digit)].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) /2

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][int(digit)], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][int(digit)].get_width()

def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collides with base or pipes."""
    pi = player['index']
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # if player crashes into ground
    if player['y'] + player['h'] >= SCREENHEIGHT:
        return [True, True]
    else:

        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])
        pipeW = IMAGES['pipe'][0].get_width()
        pipeH = IMAGES['pipe'][0].get_height()

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            uCollide = playerRect.colliderect(uPipeRect)
            lCollide = playerRect.colliderect(lPipeRect)

            if uCollide or lCollide:
                return [True, False]

    return [False, False]
    
def showGameOverScreen(crashInfo):
    """crashes the player down and shows gameover image"""
    score = crashInfo['score']
    playerx = crashInfo['x']
    playery = crashInfo['y']
    playerHeight = IMAGES['player'][0].get_height()
    playerVelY = crashInfo['playerVelY']
    playerAccY = crashInfo['playerVelY']

    upperPipes, lowerPipes = crashInfo['upperPipes'], crashInfo['lowerPipes']

    # play hit and die sounds
    SOUNDS['hit'].play()
    if not crashInfo['groundCrash']:
        SOUNDS['die'].play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery + playerHeight >= SCREENHEIGHT:
                    return
	# player velocity change
        playerVelY += playerAccY
        # player y shift till bird touches the ground
        if playery + playerHeight < SCREENHEIGHT:
            playery += playerVelY

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        showScore(score) 
	SCREEN.blit(IMAGES['player'][1], (playerx, playery))
        FPSCLOCK.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()
