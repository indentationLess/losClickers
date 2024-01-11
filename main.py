import pygame
import sys
from init import *
import math


# the display.update updates the screen in a more modern way than display.flip or something i forgot the function
# it does that by updating specific sections without affecting the rest, although leaving the function empty just
# updates the whole screen anyways.
# Aser did this ☝
def screenUpdate():
    pygame.display.update()


tacoClickCount = 0
lastPlayed = 0


# Handles mouse click events. If the close button is clicked, it terminates the game.
# it checks if the click is on the taco image and increments the taco click count accordingly.
# It also handles purchasing upgrades if the click is not on the taco image.


# Omar did this ☝
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
                if image_rect.collidepoint(mouse_pos) and menu != "shop":
                    increment = 1 + sum(
                        upgrade["effect"]
                        for upgrade in upgrades
                        if upgrade["purchased"]
                    )
                    tacoClickCount += increment
                    click.play()
                else:
                    purchaseUpgrade(mouse_pos)


# Ali did this ☝
def img(img, x, y):
    image = pygame.image.load(img)
    screen.blit(image, (x, y))


# Aser did this ☝
def displayUpgrades():
    x, y = 600, 70
    y_offset = 70
    message("Upgrades: ", black, (x, y - 50), 60)
    for upgrade in upgrades:
        status = (
            "Purchased" if upgrade["purchased"] else f"Cost: {upgrade['cost']} Clicks"
        )
        message(f"{upgrade['label']} - {status}", black, (x, y_offset), 45)


# Aser did this ☝
def displayBuildings():
    x, y = 600, 70
    y_offset = 200
    message("Buildings: ", black, (x, y_offset), 60)
    y_offset += 50
    for building in buildings:
        status = f"Purchased: {building['purchased']}, Cost: {building['cost']} Clicks"

        message(f"{building['label']} - {status}", black, (x, y_offset), 45)


# Omar did this ☝
def purchaseUpgrade(mouse_pos):
    global tacoClickCount
    x, y = 600, 50
    for upgrade in upgrades:
        text_width, text_height = screen_text.get_size()
        upgrade_rect = pygame.Rect(x, y, text_width, text_height)
        if upgrade_rect.collidepoint(mouse_pos) and not upgrade["purchased"]:
            if tacoClickCount >= upgrade["cost"]:
                tacoClickCount -= upgrade["cost"]
                upgrade["purchased"] = True
                return
        y += 150
    for building in buildings:
        text_width, text_height = screen_text.get_size()
        building_rect = pygame.Rect(x, y, 400, 60)
        if building_rect.collidepoint(mouse_pos) and tacoClickCount >= building["cost"]:
            tacoClickCount -= building["cost"]
            building["cost"] = math.floor(
                building["base_cost"] * (1.15 ** building["purchased"] + 0.25)
            )
            building["purchased"] += 1
            break
        y += 40


# Aser did this ☝
def achievmentSound():
    global lastPlayed
    if (
        tacoClickCount % 100 == 0
        and tacoClickCount != 0
        and tacoClickCount != lastPlayed
    ):
        coinUp.play()
        lastPlayed = tacoClickCount
    else:
        return


# Renders a message on the screen with specified parameters: the message text, color, coordinates, font size, and font type.
# It is used to display various texts on the screen, like the number of tacos or upgrade statuses.
# Ali did this ☝
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


# Ali did this ☝
def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Omar did this ☝
def draw_shop_button(screen, pos, pressed1, pressed3, shopClicked, menu):
    global shopBColor
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

    if (
        shopButton.collidepoint(pos)
        and pressed1
        or shopButton.collidepoint(pos)
        and pressed3
    ):
        shopClicked = True
    else:
        if shopClicked:
            menu = "shop"
        shopClicked = False

    if shopButton.collidepoint(pos):
        shopBColor = (0, 185, 0)
    else:
        shopBColor = (0, 150, 0)

    return shopClicked, menu


# Aser did this ☝
def drawBackButton(screen, pos, pressed1, backClicked, menu):
    global backBColor
    if backClicked:
        backButton = pygame.draw.rect(screen, white, (50, 100, 100, 50))
        pygame.draw.rect(screen, (0, 40, 0), (50, 140, 100, 25))
        pygame.draw.rect(screen, backBColor, (50, 100, 100, 50))
        message("Back", white, (55, 100), 50)
    else:
        backButton = pygame.draw.rect(screen, white, (50, 120, 100, 75))
        pygame.draw.rect(screen, (0, 75, 0), (50, 110, 100, 100))
        pygame.draw.rect(screen, backBColor, (50, 100, 100, 75))
        message("Back", white, (55, 120), 50)

    if backButton.collidepoint(pos) and pressed1:
        backClicked = True
    else:
        if backClicked:
            menu = "main"
        backClicked = False

    if backButton.collidepoint(pos):
        backBColor = (0, 185, 0)
    else:
        backBColor = (0, 150, 0)

    return backClicked, menu


# Omar did this ☝
def drawSaveButton(screen, pos, pressed1, pressed3, saveClicked, menu):
    global saveBColor
    if saveClicked:
        saveButton = pygame.draw.rect(screen, white, (1100, 600, 100, 50))
        pygame.draw.rect(screen, (0, 40, 0), (1100, 640, 100, 25))
        pygame.draw.rect(screen, saveBColor, (1100, 600, 100, 50))
        message("Save", white, (1105, 600), 50)
    else:
        saveButton = pygame.draw.rect(screen, white, (1100, 600, 100, 50))
        pygame.draw.rect(screen, (0, 40, 0), (1100, 640, 100, 25))
        pygame.draw.rect(screen, saveBColor, (1100, 600, 100, 50))
        message("Save", white, (1105, 600), 50)

    if (
        saveButton.collidepoint(pos)
        and pressed1
        or saveButton.collidepoint(pos)
        and pressed3
    ):
        saveClicked = True
        saveGame()

    if saveButton.collidepoint(pos):
        saveBColor = (0, 185, 0)
    else:
        saveBColor = (0, 150, 0)

    return saveClicked, menu


# Ali did this ☝
def drawLoadButton(screen, pos, pressed1, pressed3, loadClicked, menu):
    global loadBColor
    if loadClicked:
        loadButton = pygame.draw.rect(screen, white, (900, 600, 100, 50))
        pygame.draw.rect(screen, (0, 40, 0), (900, 600, 100, 25))
        pygame.draw.rect(screen, loadBColor, (900, 600, 100, 50))
        message("Load", white, (905, 600), 50)
    else:
        loadButton = pygame.draw.rect(screen, white, (900, 600, 100, 50))
        pygame.draw.rect(screen, (0, 40, 0), (900, 640, 100, 25))
        pygame.draw.rect(screen, loadBColor, (900, 600, 100, 50))
        message("Load", white, (905, 600), 50)

    if (
        loadButton.collidepoint(pos)
        and pressed1
        or loadButton.collidepoint(pos)
        and pressed3
    ):
        loadClicked = True
        loadGame()

    if loadButton.collidepoint(pos):
        loadBColor = (0, 185, 0)
    else:
        loadBColor = (0, 150, 0)

    return loadClicked, menu


# Ali did this ☝
def saveGame():
    with open("savefile.txt", "w") as file:
        data = {
            "tacoClickCount": tacoClickCount,
            "upgrades": upgrades,
            "buildings": buildings,
        }
        file.write(str(data))


# Omar did this ☝
def loadGame():
    global tacoClickCount, upgrades, buildings
    try:
        with open("savefile.txt", "r") as file:
            data = eval(file.read())
            tacoClickCount = data["tacoClickCount"]
            upgrades = data["upgrades"]
            buildings = data["buildings"]
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")


# Omar did this ☝
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill(0)
    screen.blit(background, (0, 0))
    handleEvents()
    pygame.time.delay(25)
    onclick()
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if menu == "main":
        saveClicked, menu = drawSaveButton(
            screen, pos, pressed1, pressed3, saveClicked, menu
        )
        shopClicked, menu = draw_shop_button(
            screen, pos, pressed1, pressed3, shopClicked, menu
        )
        loadClicked, menu = drawLoadButton(
            screen, pos, pressed1, pressed3, loadClicked, menu
        )
        screen.blit(taco, (taco_x, taco_y))
        image_rect = taco.get_rect()
        message(f"Tacos: {tacoClickCount}", white, (100, 60), 100)

    elif menu == "shop":
        backClicked, menu = drawBackButton(screen, pos, pressed1, backClicked, menu)
        displayUpgrades()
        displayBuildings()
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
