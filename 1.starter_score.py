from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
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
        
    # Load all the number sprites(images) into the dictionary with key = 'numbers'
    '''
    
    '''
        
    if 'win' in sys.platform:
       	soundExt = '.wav'	
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    # Create an entry into SOUNDS dictionary to store 'point' sound
    '''
    
    '''

    while True:
        mainGame()
        
def getRandomPipe():
    gapY = random.randrange(Min_PipeY, Max_PipeY) 
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, 
    ]
        

def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =  4  
    gravity    =   1   
    playerUp =  -9   
    loopIter      =   0
    playerWingPos   =   0
    score         =   0

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

	# check for score

        # Locate center of player bird's location and store it in playerMidPos
        

        # iterate over upperPipes and check whether bird crossed pipe or not, update score accordingly
        
        '''
        
        '''

        # call showScore
        	
	
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
        
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

def showScore(score):
    '''to display score in center of the screen'''
    
    # create scoreDigits to store score as a string (type cast) 

    
    # Initialize totalWidth(total width of all numbers to be printed) to 0


    # Set totalWidth according to size of digit images (use IMAGES)
    '''
    
    '''
    
    # Create Xoffset variable and initialize it to the distance from left where you want the score to appear


    # And finally blit all digits iteratively and increment Xoffset accordingly
    
    '''
    
    '''



if __name__ == '__main__':
    main()
