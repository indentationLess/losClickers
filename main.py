import pygame
import sys
from init import *


# the display.update updates the screen in a more modern way than display.flip or something i forgot the function
# it does that by updating specific sections without affecting the rest, although leaving the function empty just
# updates the whole screen anyways.
def screenUpdate():
    pygame.display.update()


tacoClickCount = 0


# Handles mouse click events. If the close button is clicked, it terminates the game.
# it checks if the click is on the taco image and increments the taco click count accordingly.
# It also handles purchasing upgrades if the click is not on the taco image.
def onclick():
    global tacoClickCount
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
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


def resize(image):
    width, height = image.get_size()
    new_width = width // 2
    new_height = height // 2
    return pygame.transform.scale(image, (new_width, new_height))


def img(img, x, y):
    image = pygame.image.load(img)
    screen.blit(image, (x, y))


def displayUpgrades():
    x, y = 600, 50  # Starting position for the upgrades menu
    y_offset = 50
    message("upgrades: ", white, (x, y - 50), 60)
    for upgrade in upgrades:
        status = (
            "Purchased" if upgrade["purchased"] else f"Cost: {upgrade['cost']} Clicks"
        )
        message(f"{upgrade['label']} - {status}", white, (x, y_offset), 60)
        y_offset += 60
    message("buildings: ", white, (x, y_offset), 60)
    y_offset += 40
    for building in buildings:
        status = (
            "Purchased: " + str(building["purchased"])
            if building["purchased"] > 0
            else f"Cost: {building['cost']} Clicks"
        )
        message(f"{building['label']} - {status}", white, (x, y_offset), 60)
    y_offset += 40


def purchaseUpgrade(mouse_pos):
    global tacoClickCount
    x, y = 400, 50
    for upgrade in upgrades:
        text_width, text_height = screen_text.get_size()
        upgrade_rect = pygame.Rect(x, y, text_width, text_height)
        if upgrade_rect.collidepoint(mouse_pos) and not upgrade["purchased"]:
            if tacoClickCount >= upgrade["cost"]:
                tacoClickCount -= upgrade["cost"]
                upgrade["purchased"] = True
                break
        y += 40
    for building in buildings:
        text_width, text_height = screen_text.get_size()
        building_rect = pygame.Rect(x, y, 400, 60)
        if building_rect.collidepoint(mouse_pos) and tacoClickCount >= building["cost"]:
            tacoClickCount -= building["cost"]
            building["purchased"] += 1
            break
        y += 40


def achievmentSound():
    if tacoClickCount % 100 == 0 and tacoClickCount != 0:
        coinUp.play()
    else:
        return


# Renders a message on the screen with specified parameters: the message text, color, coordinates, font size, and font type.
# It is used to display various texts on the screen, like the number of tacos or upgrade statuses.
def message(msg, color, cords, size, font=1):
    global screen_text
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
    message(f"tacos: {tacoClickCount}", white, (100, 60), 100)
    onclick()

    if menu == "main":
        if shopClicked:
            shopButton = pygame.draw.rect(screen, white, (1100, 100, 100, 50))
            pygame.draw.rect(screen, (0, 40, 0), (1100, 140, 100, 25))
            pygame.draw.rect(screen, shopBColor, (1100, 100, 100, 50))
            message("Shop", white, (1105, 100), 50)
        else:
            shopButton = pygame.draw.rect(screen, white, (1100, 120, 100, 75))
            pygame.draw.rect(screen, (0, 75, 0), (1100, 110, 100, 100))
            pygame.draw.rect(screen, shopBColor, (1100, 100, 100, 75))
            message("Shop", white, (1105, 120), 50)

    achievmentSound()
    screenUpdate()
    for event in pygame.event.get():
        if event.type == timer:
            for building in buildings:
                if building["label"] == "Taco Machine":
                    tacoClickCount += building["purchased"] * building["effect"]

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
