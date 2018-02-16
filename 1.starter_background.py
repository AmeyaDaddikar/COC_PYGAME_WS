#.............................First Task..................................................
#......Display the game window, load the background on it
#......The game should exit when ESCAPE is pressed or cross on the window is clicked
#......Follow the instructions given by comments on each line if you need hints
#.........................................................................................

import sys
import pygame
from pygame.locals import *

SCREENWIDTH  = 288 #size of display window
SCREENHEIGHT = 512

"""
Create a global constant 'BACKGROUND' to store the path for background image with its name with proper file extension
"""
#Your code

"""
Create an empty dictionary 'IMAGES' to store game sprites like bird, pipes, background
"""
#Your code


def main():
	global SCREEN #Global as it'll be used globally by other functions of the game instead of creating a new local copy everytime
"""
1.Intialize pygame modules
2.Set the display window of (SCREENWIDTH, SCREENHEIGHT) size to SCREEN 
3.Set the title of window as 'Flapy Bird'
4.Load the background image from its path into pygame
5.Calling ________ on images before painting the them on the display is a good practice and supports faster blitting
6.Store this final background image into the empty 'IMAGES' dictionary created above with the key 'background'
7.Call the main game
"""
#Your code


def mainGame():
"""
Condition for quitting the game
Draw images on SCREEN using the IMAGES dictionary created above and update the display
"""
#Your code


"""
........Task one is complete if you can see a display with the background on it and it closes on pressing quit or escape..........
"""

if __name__ == '__main__':
	main()
