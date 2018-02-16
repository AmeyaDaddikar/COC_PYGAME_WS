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
IMAGES = {}

#TASK1:create an empty dictionary named SOUNDS
#your code begins here

#your code ends here

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
    #TASK2:Create a tuple,into IMAGES dictionary with 'pipe' as key,which stores the pair of top and bottom pipes
    #your code begins here
    
    #your code ends here   
    
    if 'win' in sys.platform:
       	soundExt = '.wav'
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    while True:
	mainGame()


def getRandomPipe():
    """this function returns a randomly generated pipe"""

    
    #TASK3:in a variable gapY,randomly generate and store the Y coordinate
    #of the gap between upper and lower pipe,i.e. between Min_PipeY and Max_PipeY
    #your code begins here

    #your code ends here

    #TASK4:in a variable pipeHeight,store ht(pipeimage) from the pipe in IMAGES 
    #your code begins here

    #your code ends here

    #TASK5:in a variable pipeX,set the respawn x coordinate for the randomly generated pipe,preferably outside SCREENWIDTH
    #your code begins here

    #your code ends here

    #TASK6: Create and return a pair of dictionaries storing x and y coordinates of top and bottom pipes
    #These coordinates will be used to blit the pipe onto the screen later
    #the return type of this fn should be a list of a upperpipe dictionary and a lower pipe dictionary
    #your code begins here

    #your code ends here


    


def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY    =  4   # player's velocity along Y, default same as playerFlapped
    gravity    =   1   # players downward accleration
    playerUp =  -9   # players speed on flapping
    loopIter      =   0
    playerWingPos   =   0
    
    #TASK7:Generate 2 new random pipes,named newPipe1 and newPipe2,using getRandomPipe() to add to upperPipes and lowerPipes list
    #your code begins here


    #your code ends here

    #TASK8:Create 2 lists named upperPipes and lowerPipes,which stores 2 dictionaries for the 2 pipes to be loaded
    #in each dictionary,add the x,y coords of each pipe with keys 'x','y' and values as returned to newPipe1,newPipe2 
    #your code begins here



    #your code ends here

    #Velocity of pipes,pipeVelX, is a constant (Can be set variable to change difficulty)
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

	#flapping animation
        if (loopIter + 1) % 3 == 0:
            playerWingPos = next(playerFlap)
        loopIter = (loopIter + 1) % 30
        
        #TASK9:Update x coordinates of pipe according to pipeVelX
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
        #your code begins here


        #your code ends here
        #TASK10:if(its out of the screen):(1)pop the first pipe pair,(2)add a new one
        #your code begins here




        #your code ends here
        
        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerWingPos], (playerx, playery))
        
        #TASK11:Blit the upper and lower pipes on to the SCREEN
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            #your code begins here
            SCREEN.blit(    ,(  ,   ))#uPipe
            SCREEN.blit(    ,(  ,   ))#lPipe
            #your code ends here

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
