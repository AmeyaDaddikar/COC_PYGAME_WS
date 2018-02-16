#.............................Second Task..................................................
#......It's time to load the player i.e. the bird into our game
#......Subtask 1: Load the bird's images with it's flap upwards, downwards and in mid and display the bird onto the screen 
#......Subtask 2: Make the player move up if UP or SPACEBAR is pressed, else let it freefall under gravity. 
#......Subtask 3: Make the bird flap. (Hint: cycle through indices using % operator)
#......Follow the instructions given by comments on each line if you need hints
#.........................................................................................
from itertools import cycle 
"""
Cycle is a class whose object contains, you can say, a circular list. If you call the function next(cycle_object) on this object, you can iterate through the elemnts sequetially. Use this to make your bird's wings flap.
"""

import sys
import pygame
from pygame.locals import *

FPS = 30 #setting the frames per second of our game
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BACKGROUND = 'assets/sprites/background-day.png' #Specify the path where your bakcground image is stored on the computer

"""
Create a tuple PLAYER_LIST CONTAINING THE PATH OF 3 BIRD WING POSTIONS IN THE ORDER (UP,MID,DOWN)
"""
#YOUR CODE

IMAGE={} #Dictionary to store all the game sprites

"""
CREATE AN EMPTY DICTIONARY NAMED SOUNDS FOR ADDING GAME SOUNDS(similar TO THE IMAGES dcitionary created in task 1)
"""
#YOUR CODE

def main():
    global SCREEN, FPSCLOCK
    pygame.init() #Intialize pygame modules
    FPSCLOCK = pygame.time.Clock() #This returns a Clock() object to keep track of game time and stores it in FPSCLOCK
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) #This returns a window with (SCREENWIDTH, SCREENHEIGHT) dimensions
    pygame.display.set_caption('Flappy Bird') #Set the title on titlebar
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert() #load the background and convert it for faster blitting
   

    """
    1. LOAD THE 3 BIRD IMAGES FROM THE PATH YOU GAVE IN THE TUPLE CREATED ABOVE INTO PYGAME
    2. CALLING ________ on images is a good practice and retains the alpha channel of image while doing so
    IN THE IMAGES DICTIONARY, STORE THE PLAYER IMAGES YOU JUST LOADED HAVING 'player' AS THE KEY
    """
    #Your Code

    """
    1. Select sound extension(.ogg for ubuntu .wav for windows) based on windows platform and ubuntu platform
    2. Add 'wing' sound from its correct path with the correct extension according to the platform into the SOUNDS dictionary with the key 'wing'
    """
    #Your Code	
	
    while True:
        mainGame() #When you play games and lose, the game window doesn't shut abruptly, right? It allows you to start a new game by pressing some 'back' button.Similarly, mainGame is inside an infinite loop so that if you lose the game(by crashing or collision), the program should allow you to play again, the program shouldn't abruptly end when you crash. You should be able to re-play your game without having to actually run the program again. It'll be more clear once you build the entire game

def mainGame():
    playerFlap = cycle([0, 1, 2, 1]) #Returns a cycle object and stores it in playerFlap. Now you can call next(playerFlap) to cycle through the values [0, 1, 2, 1]
    playerx, playery = SCREENWIDTH*0.2, SCREENHEIGHT/2 #player's inital position on SCREEN before the game begins
    playerVelY       =   4   # player's velocity along Y(remember downward is positive Y axis and towards right is positive X axis)
    gravity          =   1   # player's downward accleration(think why is it positive?)
    playerUp         =  -9   # player's speed on pressing UP key(think why is it negative?)
    loopIter         =   0   # helper variable to make the bird 'flap' its wings
    playerWingPos    =   0   # Variable that determines which wing position to draw on the SCREEN, whether it is UP or MID or DOWN, initally we start with UP position

    while True: #the actual game loop
        
    	for event in pygame.event.get(): #get() function returns a list of all events captured by pygame
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): #to exit the game
                pygame.quit()
                sys.exit()
		
            """
            1.INSIDE THIS FOR LOOP, CHECK IF SPACEBAR OR THE UP KEY IS PRESSED
            2.IF PRESSED, MAKE THE BIRD MOVE UP AND PLAY THE BIRD FLAPPING SOUND 
	    3.PLAY THE FLAPPING SOUND 'wing' FROM THE SOUNDS DICTIONARY CREATED ABOVE
            """
	    #Your code
		
        """
        OUTSIDE THE EVENTS LOOP
        1.UPDATE THE PLAYER'S VERTICAL VELOCIY BY ADDING GRAVITY FOR FREEFALL(Velocity increases while falling right?)
        2.NOW UPDATE THE PLAYER'S ACTUAL Y COORDINATE USING PLAYER'S VERTICAL VELOCITY
	"""
	#Your code

	
        """
        DECIDING WHICH PLAYER IMAGE TO DRAW ON SCREEN UP FLAP/MID FLAP/DOWN FLAP 
        1.USING THE loopIter VARIABLE, CHANGE THE playerWingPos ACCORDINGLY(0 OR 1 OR 2)
        """
	#Your code
	
        SCREEN.blit(IMAGES['background'], (0,0)) #Constantly repaint the background to erase previous images of game assets
        
	"""
        1.DRAW THE SELECTED PLAYER IMAGE ON THE SCREEN AT THE COORDINATE player,playery
        """
	#Your code
	
        pygame.display.update()
        FPSCLOCK.tick(FPS) #This will ensure your game runs at no more than 'FPS' frames per second, basically controls the game speed

	
"""
............Task two is complete if you can control the bird with UP or SPACEBAR KEY with the 'wing' sound being played, if neither of these keys are pressed, the bird will freefall under gravity. Also, the wings flap after some interval.......................
"""
if __name__ == '__main__':
    main()
