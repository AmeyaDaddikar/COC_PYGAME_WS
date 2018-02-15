import sys
import pygame
from pygame.locals import *


SCREENWIDTH  = 288
SCREENHEIGHT = 512

######BACKGROUND = 'assets/sprites/background-day.png' ##khud load karo

#dictionary to store all game sprites
########IMAGES = {} ##khud load karo##khud load karo

def main():
#####ADD EXACT COMMENTS
    '''
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()

    while True:

        mainGame() 
    '''    

def mainGame():
    '''
    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        SCREEN.blit(IMAGES['background'], (0,0))
        pygame.display.update()
     '''
        


if __name__ == '__main__':
    main()
