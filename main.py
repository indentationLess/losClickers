import pygame
import os
from init import *


def screenUpdate():
    pygame.display.update()


tacoClickCount = 0


def onclick():
    global tacoClickCount
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if image_rect.collidepoint(mouse_pos):
                    increment = 1 + sum(
                        upgrade["effect"]
                        for upgrade in upgrades
                        if upgrade["purchased"]
                    )
                    tacoClickCount += increment
                    click.play()
                else:
                    purchaseUpgrade(mouse_pos)


def displayUpgrades():
    x, y = 400, 50  # Starting position for the upgrades menu
    for upgrade in upgrades:
        status = (
            "Purchased" if upgrade["purchased"] else f"Cost: {upgrade['cost']} Clicks"
        )
        message(f"{upgrade['label']} - {status}", white, (x, y), 30)
        y += 40


def purchaseUpgrade(mouse_pos):
    global tacoClickCount
    x, y = 400, 50
    for upgrade in upgrades:
        upgrade_rect = pygame.Rect(x, y, 200, 30)
        if upgrade_rect.collidepoint(mouse_pos) and not upgrade["purchased"]:
            if tacoClickCount >= upgrade["cost"]:
                tacoClickCount -= upgrade["cost"]
                upgrade["purchased"] = True
                break
        y += 40


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

    pygame.time.delay(25)
    # Display the image on the window
    screen.blit(taco, (taco_x, taco_y))
    image_rect = taco.get_rect()
    image_rect.center = (400, 300)
    message(f"tacos: {tacoClickCount}", white, (100, 60), 100)
    onclick()
    displayUpgrades()
    screenUpdate()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
