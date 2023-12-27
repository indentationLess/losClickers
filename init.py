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
taco_width = taco.get_width()
taco_height = taco.get_height()
taco_rect = taco.get_rect()

taco_x = 50
taco_y = 80
# for text
black = (0, 0, 0)
white = (255, 255, 255)

# upgrades list
upgrades = [{"cost": 25, "effect": 1, "purchased": False, "label": "Double Click"}]
buildings = [
    {"cost": 100, "effect": 1, "purchased": 0, "label": "taco machine"},
]

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)
