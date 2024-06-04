import pgzrun
import pygame

## WARNING ##
# 
# Parts of this code were written by AI but they were reviewed and fixed by humans :)
#
## WARNING ##

# Set the dimensions of the window
WIDTH = 640
HEIGHT = 480

def draw():
    screen.fill((255, 255, 255))  # Fill the screen with white color
    screen.blit(miku.png, (WIDTH/2, HEIGHT/2))  # Display the image at the center

def update():
    draw()
    pass  # Add any game logic or updates here

pgzrun.go()
