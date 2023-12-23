import pygame
import os
from init import * 

# Get the dimensions of the image
taco_width  = taco.get_width()
taco_height = taco.get_height()

taco_x = width // 2 - taco_width // 2
taco_y = height // 2 - taco_height // 2

def onclick():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if image_rect.collidepoint(mouse_pos):
                        print("Image clicked!")


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
    image_rect = taco.get_rect()
    image_rect.center = (400, 300) 
    onclick()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

