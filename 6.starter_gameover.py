#.............................Final Task..................................................
#......Our game is almost complete! We just need to make the bird fall under gravity if it's pipe crash
#......Whether it's pipe crash or ground crash, we need to stop the game and allow the player to play again if he presses ESCAPE or UP key
#......Follow the instructions given by comments on each line if you need hints
#.........................................................................................
from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *


FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND   = 'assets/sprites/background-day.png'
PIPEGAPSIZE  = 100 
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

    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
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
        
    if 'win' in sys.platform:
       	soundExt = '.wav'	
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)
    SOUNDS['point']   = pygame.mixer.Sound('assets/audio/point' + soundExt)
    SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt)
    SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)
    
    while True:
        #mainGame()
        '''
        Change the above code to store the dictionary returned by mainGame() function
        Call showGameOverScreen(your_mainGame_dictionary) to end the game
	'''
def getRandomPipe():
    """returns a randomly generated pipe"""
    gapY = random.randrange(Min_PipeY, Max_PipeY) 
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]

def showScore(score):
    """displays score in center of screen"""
    scoreDigits = str(score)
    totalWidth = 0 

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][int(digit)].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) /2

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][int(digit)], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][int(digit)].get_width()


def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY       =   4   
    gravity          =   1   
    playerUp         =  -9 
    loopIter         =   0
    playerWingPos    =   0
    score            =   0
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [
        {'x': newPipe1[0]['x'] , 'y': newPipe1[0]['y']},
        {'x': newPipe2[0]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]

    lowerPipes = [
        {'x': newPipe1[1]['x'] , 'y': newPipe1[1]['y']},
        {'x': newPipe2[1]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerUp
                SOUNDS['wing'].play()
        playerVelY += gravity
        playery += playerVelY

        crashTest = checkCrash({'x': playerx, 'y': playery},
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
                'playerVelY': gravity
            }

        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 3:
                score += 1
                SOUNDS['point'].play()
	
        if (loopIter + 1) % 3 == 0:
            playerWingPos = next(playerFlap)
        loopIter = (loopIter + 1) % 30
        
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX
	
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width(): 
            upperPipes.pop(0)
            lowerPipes.pop(0)
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])
        

        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerWingPos], (playerx, playery))
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))
	showScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collides with base or pipes."""
    #Store bird's height and width
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # if player has touched the ground
    if player['y'] + player['h'] >= SCREENHEIGHT:
        return [True, True] #second True is for ground crash
    else:
        #if not ground crash then see if it's collision with pipe
        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h']) #Draw rectangle around player
        pipeW = IMAGES['pipe'][0].get_width() 
        pipeH = IMAGES['pipe'][0].get_height()

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            #Draw rectangle around upper and lower pipes
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            uCollide = playerRect.colliderect(uPipeRect) #if the bird rectangle has collided with upper pipe rectangle
            lCollide = playerRect.colliderect(lPipeRect) #if the bird rectangle has collided with upper pipe rectangle

            if uCollide or lCollide:
                return [True, False] #False means it is not ground collision but a pipe collision

    return [False, False]
    
def showGameOverScreen(crashInfo):
    """crashes the player down if it is pipe collision"""
    '''
    1.Create variables to store all the data passed into crashInfo,
    score, playerx, playery, playerVelY, gravity=playerVelY, upperPipes, lowerPipes
    2.Get player height from IMAGES
    3.Play hit sound
    4. If it is pipe crash, play 'die' sound as well

    '''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                """
		If the player has pressed UP or SPACEBAR and
		if the player has reached the ground(by ground collision or by freefall from hitting any pipe):
		return to the main function() so that he can play again(Remember the infinite while loop?)
		"""
        
        '''
        Make playery increase with increasing velocity(use gravity) until bird touches the ground
        '''
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

