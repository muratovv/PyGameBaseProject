__author__ = 'Федор'
"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from pyGameDir.space import Space
import math
# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

pygame.init()

# Set the width and height of the screen [width, height]
resolution = [1024, 768]
size = (resolution[0], resolution[1])
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
pygame.mouse.set_visible(1)
#Loop until the user clicks the close button.

def draw_stick_figure(screen, x, y):
    # Голова
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)

    # Ноги
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 2)

    # Тело
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)

    # Руки
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)


spaceAnimation = Space(resolution, 150, 10)
done = False
fi = 0
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    screen.fill(BLACK)
    spaceAnimation.action(screen)
    spaceAnimation(fi/10)
    fi += 0.1
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

