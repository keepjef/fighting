import pygame
from character import Character
import math
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
batman = Character("Batman", 100, 100, 350, image=image, strength=10, sprites=sprite_scale)
exit = False
clock = pygame.time.Clock()
count = 0
on_ground = True
jump_height_flag = False

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
            jump_height_flag = True
            jump_height = batman.y - 100
            velocity = 5
            a = 25
            on_ground = False

    if on_ground == False and jump_height_flag == True:
        velocity = velocity + math.sqrt(a)
        batman.y = batman.y - velocity
        if batman.y <= jump_height:
            velocity = 0
            a = 0.6
            jump_height_flag = False

    elif on_ground == False:
        batman.y = batman.y + velocity
        velocity = velocity + a**2
        if batman.y >= height-250:
            on_ground = True
    display.blit(batman.sprites[count],(batman.x,batman.y))
    pygame.display.update()
