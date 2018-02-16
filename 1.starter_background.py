#.............................First Task..................................................
#......Display the game window, load the background on it
#......The game should exit when ESCAPE is pressed or cross on the window is clicked
#......Follow the instructions given by comments on each line if you need hints
#.........................................................................................

import sys
import pygame
from pygame.locals import *

SCREENWIDTH  = 288
SCREENHEIGHT = 512

#Create a global constant to store the path for background image with its name with proper file extension

#Create an empty dictionary to store game sprites like bird, pipes, background

def main():
	global SCREEN #Global as it'll be used globally by other functions of the game instead of creating a new local copy everytime
#Intialize pygame modules
#Set the display window of appropriate size to SCREEN 
#Set the title of window as 'Flapy Bird'
#Load the background image from its path into pygame
#Doing ________ on images before painting the them on the display is a good practice and supports faster blitting
#Store this final background image into the empty dictionary created above with the key 'background'
#Call the main game
     

def mainGame():
#Condition for quitting the game
#Draw images on SCREEN using the dictionary created above and update the display
     

#-........Task one is complete if you can see a display with the background on it and it closes on pressing quit or escape..........
if __name__ == '__main__':
	main()
