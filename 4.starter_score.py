#.............................Fourth Task..................................................
#......We now need to keep scores of our game
#......Subtask 1: Load the bird's images with it's flap upwards, downwards and in mid and display the bird onto the screen 
#......Subtask 2: Make the player move up if UP or SPACEBAR is pressed, else let it freefall under gravity. 
#......Subtask 3: Make the bird flap. (Hint: cycle through indices using % operator)
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
    """  
    Load all the number sprites(images) into the dictionary with key = 'numbers' 
    """
    #Your code
        
    if 'win' in sys.platform:
       	soundExt = '.wav'	
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    """
    Create an entry into SOUNDS dictionary to store 'point' sound with key 'point'
    """
    #Your code

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

        """
        Locate center of player bird's location and store it in playerMidPos
	"""
	#Your code
        
        """
        1.Iterate over upperPipes 
	2.Check whether the bird crossed pipe's mid or not 
	3.Update score accordingly
	4.Play the 'point' sound
        """
	#Your code
        
        
       
        """
        Call showScore() which will display your score with the help of number sprites
	"""
	#Your Code
        	
	
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
    """to display score in center of the screen"""
    """
    Create scoreDigits to store each digit of score as a string 
    E.g. the score is 23 then scoreDigits should treat '2' and '3' separately as we've to display these numbers separately
    (There is no sprite '23' there is only '2' and '3')
    """
    #Your code

    """
    Initialize totalWidth(total width of all numbers to be printed) to 0
    """
    #Your code

    """
    Set totalWidth according to size of digit images (use IMAGES dictionary)
    E.g. for 23, you need the width of '2' and '3' so width('2') + width('3') will be your totalWidth
    Hint: You can iterate over strings just like you can iterate over lists
    """
    #Your code
    
    
    """
    Create Xoffset variable and initialize it to the distance from left where you want the first digit of score to appear
    """
    #Your code

    """
    # And finally blit all digits iteratively and increment Xoffset accordingly for subsquent digitis of score
    
    """
    #Your code

"""
........Task four ends when each time the bird crosses a pipe's mid, the score updates with the point sound being played and the score appears at the top of the screen at center

"""

if __name__ == '__main__':
    main()
