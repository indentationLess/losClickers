import pygame
import os
from init import *


def screenUpdate():
    pygame.display.update()


def onclick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if image_rect.collidepoint(mouse_pos):
                    print("Image clicked!")


def message(msg, color, cords, size, font=1):
    fontsize = int(size)
    if font == 1:
        font = pygame.font.SysFont(None, fontsize)
    elif font == 2:
        font = pygame.font.SysFont("dejavuserif", fontsize)
    elif font == 3:
        font = pygame.font.SysFont("dejavusansmono", fontsize)
    elif font == 4:
        font = pygame.font.SysFont("dejavusans", fontsize)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, cords)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(0)
    screen.blit(background, (0, 0))

    pygame.time.delay(10)
    # Display the image on the window
    screen.blit(taco, (taco_x, taco_y))
    image_rect = taco.get_rect()
    image_rect.center = (400, 300)
    message("taco", white, (taco_x, taco_y + 20), 50)

    onclick()

    screenUpdate()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
