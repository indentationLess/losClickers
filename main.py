# Example file showing a circle moving on screen
import pygame
import os
# pygame setup
pygame.init()
width = 1280 
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
# pygame.display.set_icon("resources/images/favicon.ico").convert()
pygame.display.set_caption("IT'SSSSSSSSSSSSSSSSSS LOSCLICKERS")
running = True
dt = 0

# sounds !!
coinUp = pygame.mixer.Sound('resources/sounds/pickupCoin.wav')
click = pygame.mixer.Sound('resources/sounds/click.wav')
coinUp.set_volume(0.3)
click.set_volume(0.3)

# images !!
image = pygame.image.load('resources/images/background.jpg')
background = pygame.transform.scale(image, (width, height))
taco = pygame.image.load('resources/images/taco.png')
# Get the dimensions of the image
taco_width  = taco.get_width()
taco_height = taco.get_height()

taco_x = width // 2 - taco_width // 2
taco_y = height // 2 - taco_height // 2

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(0)
    screen.blit(background, (0, 0))
    # Display the image on the window
    screen.blit(taco, (taco_x, taco_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

