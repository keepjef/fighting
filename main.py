import pygame
from character import Character
pygame.init()
width = 1000
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fight club")
image = pygame.image.load("assets/images/img.png")
sprites = [
    pygame.image.load("assets/images/walking se0000.bmp"),
    pygame.image.load("assets/images/walking se0001.bmp"),
    pygame.image.load("assets/images/walking se0002.bmp"),
    pygame.image.load("assets/images/walking se0003.bmp"),
    pygame.image.load("assets/images/walking se0004.bmp"),
    pygame.image.load("assets/images/walking se0005.bmp"),
    pygame.image.load("assets/images/walking se0006.bmp"),
]
sprite_scale = [pygame.transform.scale(image, (200,200)) for image in sprites]
batman = Character("Batman", 100, 100, 100, image=image, strength=10, sprites=sprite_scale)
exit = False
clock = pygame.time.Clock()
count = 0
on_ground = True


while not exit:
    clock.tick(30)
    display.fill('green')
    count += 1
    if count == len(batman.sprites):
        count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            batman.x = batman.x - 5
        if keys[pygame.K_RIGHT]:
            batman.x = batman.x + 5
        if keys[pygame.K_UP]:
            batman.y = batman.y - 5
        if keys[pygame.K_DOWN]:
            batman.y = batman.y + 5
        if keys[pygame.K_SPACE] and on_ground == True:
            batman.y = batman.y - 250
            velocity = 0
            a = 0.3
            on_ground = False
    if on_ground == False:
        batman.y = batman.y + velocity
        velocity = velocity + a**2
        if batman.y >= height-200:
            on_ground = True
    display.blit(batman.sprites[count],(batman.x,batman.y))
    pygame.display.update()