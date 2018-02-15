import sys
import pygame
from pygame.locals import *


SCREENWIDTH  = 288
SCREENHEIGHT = 512

### Create a global constant which stores a string path to the background image
######BACKGROUND = 'assets/sprites/background-day.png' ##khud load karo

### Create an empty dictionary to store all game sprites 
########IMAGES = {} ##khud load karo##khud load karo

def main():
#####ADD EXACT COMMENTS
    global SCREEN    ### Use to declare usage of global SCREEN here instead of creating a new local copy
    '''
    ###Initialize pygame
    pygame.init()

    ###Initialize SCREEN using set_mode
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    ###Set window caption as 'Flappy Bird'
    pygame.display.set_caption('Flappy Bird')

    ###Doing ____ on images is a good practice and supports faster blitting
    ###Add the converted image to the empty dictionary created above with the key 'background'
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()

    ###Call mainGame function inside an infinite loop
    while True:

        mainGame() 
    '''    

def mainGame():
    '''
    ###Create an infinite game loop and write quit events to exit game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        ### Draw images on SCREEN using dictionary created above
        SCREEN.blit(IMAGES['background'], (0,0))

        ### Update display
        pygame.display.update()
    '''
        


if __name__ == '__main__':
    main()
