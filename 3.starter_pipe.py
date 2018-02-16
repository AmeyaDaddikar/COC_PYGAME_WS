#.............................Third Task..................................................
#......Now we render our pipes 
#......1.We first load images of upper and lower pipes into pygame. 
#......2.Create a new function which returns a pair of pipes(i.e. uppar and lower pipe) with it's x,y coordinate.
#......3.Use the coordinates of pipe returned by this function to blit them onto display.
#......4.Remove and add new pipes as the game progresses.
#......5.Don't forget to make the pipes move too!
#.........................................................................................
from itertools import cycle
import sys
import pygame
import random
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png'
PIPEGAPSIZE  = 100 # gap between lower part of upper and upper part of lower part of pipe
Max_PipeY    =  220 # range for pipe gap's Y coordinate
Min_PipeY    =  100

PLAYERS_LIST = (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png')
PIPE = 'assets/sprites/pipe-green.png'
IMAGES = {}
SOUNDS = {} #Empty dictionary to store game sounds

def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
#load the bird in 3 different wing positions and convert_alpha to convert it while retaining the the alpha channel(Remember convert() functions removed an image's alpha channel if it was present in it and then performed the conversion?Hence use convert_alpha)
    IMAGES['player'] = (  
            pygame.image.load(PLAYERS_LIST[0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[2]).convert_alpha(),
        )
    """
    SUBTASK1:Create a tuple,into IMAGES dictionary with 'pipe' as key,which stores the pair of top and bottom pipes. 
    Remember we've only ONE pipe image. 
    """
    #your code begins here
    
    #your code ends here   
    
    if 'win' in sys.platform: #if the OS is windows, use .wav extension else use .ogg sound extension
       	soundExt = '.wav'
    else:
        soundExt = '.ogg'
    SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt) #load sound from its path into pygame with correct extension

    while True:
	mainGame()


def getRandomPipe():
    """this function returns a randomly generated pipe"""

    """
    SUBTASK2:In a variable gapY,randomly generate and store the Y coordinate of the gap  between upper and lower pipe(top Y coordinate of the gap is nothing but bottom y coordinate of upper pipe). This random Y coordinate should be in the range of Min_PipeY and Max_PipeY(Guess why we've imposed the range constraint?)
    """
    #your code begins here

    #your code ends here
	
    """"
    #SUBTASK3:in a variable pipeHeight,store height of pipe from pipe image in IMAGES 
    """
    #your code begins here

    #your code ends here

    """
    SUBTASK4:in a variable pipeX,set the respawn x coordinate for the randomly generated pipe,preferably outside SCREENWIDTH(Do you want the pipe to suddenly appear on the SCREEN out of nowhere?)
    """
    #your code begins here

    #your code ends here

    """
    SUBTASK5: Create and return a pair of dictionaries storing x and y coordinates of top and bottom pipes
    These coordinates will be used to blit the pipe onto the screen later
    The return type of this fn should be a list of a upperpipe dictionary and a lower pipe dictionary
    """
    #your code begins here

    #your code ends here


    


def mainGame():
    playerFlap = cycle([0, 1, 2, 1])
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2
    playerVelY       =   4  
    gravity          =   1   
    playerUp         =  -9   
    loopIter         =   0
    playerWingPos    =   0
    
    """
    SUBTASK6:Generate 2 new random pipes,named newPipe1 and newPipe2,using getRandomPipe() to add to upperPipes and lowerPipes list
    """
    #your code begins here


    #your code ends here

    """
    SUBTASK7:Create 2 lists named upperPipes and lowerPipes,which stores 2 dictionaries for the 2 pipes to be loaded. In each dictionary,add the x,y coords of each pipe with keys 'x','y' and values as returned to newPipe1,newPipe2 by the randomPipe() fucntion
    """
    #your code begins here



    #your code ends here

    #Velocity of pipes,pipeVelX, is a constant (Can be set variable to change difficulty of your game)
    pipeVelX = -4


    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
	    if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
		playerVelY = playerUp #Make the bird accelerate in upward direction
                SOUNDS['wing'].play()
        playerVelY += gravity #freefall 
        playery += playerVelY #actually make the bird fall by changing its y coordinate

	#flapping animation
        if (loopIter + 1) % 3 == 0:
            playerWingPos = next(playerFlap)
        loopIter = (loopIter + 1) % 30
        
	"""
        SUBTASK8:Update x coordinates of pipe according to pipeVelX, just like you updated the coordinates of bird's image
	"""
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
        #your code begins here


        #your code ends here
	"""
        SUBTASK9:if(pipe out of the screen):
	1.pop the first pipe pair
	2.add a new one
	"""
        #your code begins here




        #your code ends here
        
        SCREEN.blit(IMAGES['background'], (0,0))
	SCREEN.blit(IMAGES['player'][playerWingPos], (playerx, playery))
        
	"""
        SUBTASK10:Blit the upper and lower pipes on to the SCREEN
	"""
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            #your code begins here
            SCREEN.blit(    ,(  ,   ))#uPipe
            SCREEN.blit(    ,(  ,   ))#lPipe
            #your code ends here

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
