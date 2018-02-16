#.............................Fifth Task..................................................
#......We now check for collision between bird and pipes or ground
#......We first check if there's any collision at all
#......If there's collision then whether it's ground collision or pipe collision
#......If it's pipe collision, we make it fall under gravity
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
    while True:
    	mainGame()

def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =   4
    gravity       =   1   
    playerUp      =  -9   
    loopIter      =   0
    playerWingPos =   0
    score         =   0
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    upperPipes = [
        {'x': newPipe1[0]['x'] , 'y': newPipe1[0]['y']},
        {'x': newPipe1[0]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ] 
    lowerPipes = [
        {'x': newPipe1[1]['x'] , 'y': newPipe1[1]['y']},
        {'x': newPipe1[1]['x'] + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ] 

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

        """
	We check for crash here. To do so, we'll pass the coordinates of bird and all the pipes in the screen
	If there's any collision i.e. if crashTest[0] is True, e return to the main() function to show gameover(sixth task)
	"""
        crashTest = checkCrash({'x': playerx, 'y': playery},
                               upperPipes, lowerPipes)
        if crashTest[0]:
            return {
                'y': playery,
                'groundCrash': crashTest[1],
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'score': score,
                'playerVelY': playerVelY,
            }

	#Locate the player center's x position on the SCREEN
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
	
	#If the player's center has crossed any pipe's center, update the score and play 'point' sound
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
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
        
def getRandomPipe():
    """returns a randomly generated pipe"""
    gapY = random.randrange(Min_PipeY, Max_PipeY) 
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10
    
    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, 
    ]
    
def showScore(score):
    """displays score in center of screen"""
    scoreDigits = str(score)
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][int(digit)].get_width() #determine the width of all digit images in score

    Xoffset = (SCREENWIDTH - totalWidth) /2 #The distance from left a which you want to display each digit from scoreDIgits

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][int(digit)], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][int(digit)].get_width() #skip the distance occupied by current score digit and render the next score digit at this nw Xoffset position



def checkCrash(player, upperPipes, lowerPipes):
    '''
    """checks if the player has crashed with any object or the ground."""

        The function returns a list of boolean values.
        Following are the possible returned values

        1. [True, True]    : player has collided with the ground   
        2. [True, False]   : player has collided with a pipe
        3. [False,False]   : player hasn't collided with anything

    NOTE : The function should not return [False, True] as it is an invalid state,
    i.e. the return value will not make any sense.
    '''

    # Assigns the width and the height of the player hit-box as per it's image asset.
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # Check if the player crashes into ground.
    '''
    # CODE_BLOCK1
    
    If this box is representing the player, then the top-left co-ordinate is player['x'], player['y']
    If the height of the box is player['h'], what must be the y-co-ordinate of the bottom point? 
    (Remember, (0,0) i.e. the origin is on the top -left of the screen always, and 
    THE Y-AXIS IS INCREASING DOWNWARDS POSITIVELY)

            .-----.
            .     .
            .     .
            .-----.
        _________________
            
    Another question, if the player hits the ground, then wouldn't the Y-co-ordinate of the player exceed
    to the Y-co-ordinate of the ground, or perhaps the screen?

    # Uncomment the code in CODE_BLOCK1 and replace CHECK_PLAYER_GROUND_CRASH with the actual condition.

    if CHECK_PLAYER_GROUND_CRASH:
        return [True, True]
    
    # CODE_BLOCK1 ENDS HERE. UNCOMMENT TILL HERE ONLY FOR CODE_BLOCK1
    '''

    '''
    CODE_BLOCK1 code is successful if your game stops once the player hits the ground
##########################################################################################################
##########################################################################################################

    CODE_BLOCK2 is all about checking whether the player hits the pipes. The pipes are of
    two types, viz upperPipes(list of upper pipes) and the lowerPipes(list of lower pipes) 

    '''

    '''
    CODE_BLOCK2

    1. CREATE a playerRect which is a rectangle surrounding the player.
    Use pygame.Rect() for that.
        
        pygame.Rect(x,y,w,h)
            x --- top-left x-co-ordinate of the rectangle
            y --- top-left y-co-ordinate of the rectangle
            w --- width  of the rectangle
            h --- height of the rectangle
    
    2. get the pipeW(pipe width) and pipeH(pipe height) from the pipe image asset.
    HINT: Get the pipeW and pipeH the same way you got player['w'] and player['h']

    3. For every uPipe in upperPipes and every lPipe in lowerPipes, create a rectangle
    using pygame.Rect() 
    
    4. Collsion Detection
    So, suppose you made a rectangle for uPipe called uPipeRect.
    You have to check it's collisions with the playerRect.
    you can do that using

    playerRect.colliderect(uPipeRect)

    This returns a true/false value depending on whether the collision occured.
    Do the same for the lPipe too.
    
    Replace COLLISION_WITH_A_PIPE_OCCURS with your conditions, and add all the loops/ if else
    blocks as per your necessity.

        if COLLISION_WITH_A_PIPE_OCCURS:
            return [True, False]
    '''


    # No collision with pipes or the ground. Starter code will by default return False,False
    #Follow instructions to add checks for collisions accordingly.            
    return [False, False]

"""
..............Task five ends when your game stops on collision with pipes or on hitting the ground during freefall...............
"""

if __name__ == '__main__':
    main()
