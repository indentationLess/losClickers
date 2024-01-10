import pygame

# setup stuff
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("IT'SSSSSSSSSSSSSSSSSS LOSCLICKERS")
running = True
dt = 0

# sounds !!
coinUp = pygame.mixer.Sound("resources/sounds/pickupCoin.wav")
click = pygame.mixer.Sound("resources/sounds/click.wav")
coinUp.set_volume(1)
click.set_volume(1)

# images !!
image = pygame.image.load("resources/images/background.jpg")
background = pygame.transform.scale(image, (width, height))
taco = pygame.image.load("resources/images/taco.png")

# Get the dimensions of the image
taco_width, taco_height = taco.get_size()
taco_rect = taco.get_rect()

taco_x = 50
taco_y = 80
# for text
black = (0, 0, 0)
white = (255, 255, 255)

# upgrades list
upgrades = [{"cost": 25, "effect": 1, "purchased": False, "label": "Double Click"}]
buildings = [
    {"base_cost": 15,"cost": 15, "effect": 1, "purchased": 0, "label": "Taco Machine"},]
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 500)

# game menus !!
menu = "main"

shopClicked = False
shopBColor = (0, 150, 0)

backClicked = False
backBColor = (0, 150, 0)

sellClicked = False
sellBColor = (0, 150, 0)

UpgradeClicked = False
UpgradeBColor = (0, 150, 0)

TacoMakers = [0, 0, 0, 0, 0, 0]
