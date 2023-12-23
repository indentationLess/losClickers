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


# for text 
black = (0,0,0)
white = (255,255,255)