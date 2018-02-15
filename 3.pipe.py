from itertools import cycle
import sys
import pygame
import random
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
BASEY        = SCREENHEIGHT * 0.79
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
Max_PipeY    =  220 # range for pipe gap's top most x,y
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
        '''
    ### Create a tuple storing the pair of top and bottom pipes and store it into IMAGES with 'pipe' key
    IMAGES['pipe'] = (
            pygame.transform.rotate(
                pygame.image.load(PIPE).convert_alpha(), 180),
            pygame.image.load(PIPE).convert_alpha(),
        ) 
        '''
    if 'win' in sys.platform:
       	soundExt = '.wav'
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    while True:
	mainGame()
	
        
def getRandomPipe():
    """returns a randomly generated pipe"""
    '''
    # height of gap between upper and lower pipe
    ### generate a random coordinate for bottom left corner of top pipe between Min_PipeY and Max_PipeY 
    gapY = random.randrange(Min_PipeY,Max_PipeY) #Range for bottom left most y coordinate of upper pipe 

    ### Calculate pipe height from the image of pipes
    pipeHeight = IMAGES['pipe'][0].get_height()

    ### Set a random coordinate for pipeX preferably outside the SCREENWIDTH
    pipeX = SCREENWIDTH + 10
    
    ### Create and return a pair of dictionaries storing x and y coordinates of top and bottom pipes
    ### These coordinates will be used to blit the pipe onto the screen later
    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]
    '''


def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =  4   # player's velocity along Y, default same as playerFlapped
    gravity    =   1   # players downward accleration
    playerUp =  -9   # players speed on flapping
    loopIter      =   0
    playerWingPos   =   0
    '''
    # get 2 new pipes to add to upperPipes lowerPipes list
    ### Generate a random pipe using the function created above
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipes
    ### Create a list of Upper pipes(as dictionaries returned by getRandomPipe())
    ### and set correct x coordinates 
    upperPipes = [
        {'x': newPipe1[0]['x'] , 'y': newPipe1[0]['y']},
        {'x': newPipe2[0]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ] #inital position of two upper pipes

    # list of lowerpipe
    ### Create a list of Lower pipes same as above
    lowerPipes = [
        {'x': newPipe1[1]['x'] , 'y': newPipe1[1]['y']},
        {'x': newPipe2[1]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ] #inital position of two lower pipes

    '''
    ### Velocity of pipes is a constant (Can be set variable to change difficulty)
    pipeVelX = -4


    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerUp #accelerate karvao
                SOUNDS['wing'].play()
        playerVelY += gravity
        playery += playerVelY
	
	#in simple terms, player wing flap karane 
        if (loopIter + 1) % 3 == 0:
            playerWingPos = next(playerFlap)
        loopIter = (loopIter + 1) % 30
        '''
        ### Change x coordinates of pipe according to pipeVelX 
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX
	
        # remove first pipe if its out of the screen and add new one 
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width(): #obviously -(width) hi hoga
            upperPipes.pop(0)
            lowerPipes.pop(0)
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])
        '''
        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerWingPos], (playerx, playery))
        '''
        ### Blit the 2 upper and lower pipes on to the SCREEN
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))
        '''
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
