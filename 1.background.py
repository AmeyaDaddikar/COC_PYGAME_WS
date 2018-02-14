import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512

BACKGROUND = 'assets/sprites/background-day.png'

#dictionary to store all game sprites
IMAGES = {}

def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock() #to track time
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()

    while True:

        mainGame()

def mainGame():
    while True:
    	for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        SCREEN.blit(IMAGES['background'], (0,0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
