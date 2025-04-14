import pygame
from character import Character

pygame.init()
width = 1000
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fight Club")

# Загрузка изображений
image = pygame.image.load("assets/images/img.png")
run_sprites = [
    pygame.image.load("assets/Fighter sprites/fighter_run_0024.png"),
    pygame.image.load("assets/Fighter sprites/fighter_run_0018.png"),
    pygame.image.load("assets/Fighter sprites/fighter_run_0019.png"),
    pygame.image.load("assets/Fighter sprites/fighter_run_0020.png"),
    pygame.image.load("assets/Fighter sprites/fighter_run_0021.png"),
    pygame.image.load("assets/Fighter sprites/fighter_run_0022.png"),
    pygame.image.load("assets/Fighter sprites/fighter_run_0023.png"),
]
attack_sprites = [
    pygame.image.load("assets/Sword sprites/sword_air_attack_0063.png"),
    # Добавьте больше спрайтов атаки для анимации
]
jump_sprites = [
    pygame.image.load("assets/Fighter sprites/fighter_jump_0043.png"),
    pygame.image.load("assets/Fighter sprites/fighter_jump_0044.png"),
    pygame.image.load("assets/Fighter sprites/fighter_jump_0045.png"),
    pygame.image.load("assets/Fighter sprites/fighter_jump_0046.png"),
    pygame.image.load("assets/Fighter sprites/fighter_jump_0047.png"),
]

# Создание персонажей
batman = Character("Batman", 100, 20, 200, image, 10, run_sprites, attack_sprites, jump_sprites)
spider_man = Character("Spider-Man", 100, 20, 200, image, 10, run_sprites, attack_sprites, jump_sprites)

exit = False
clock = pygame.time.Clock()

while not exit:
    clock.tick(40)
    display.fill('green')
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(200, 200, 200, 200))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # Управление Бэтменом
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        batman.x -= 5
        batman.state = 'running'
    elif keys[pygame.K_RIGHT]:
        batman.x += 5
        batman.state = 'running'
    else:
        if batman.state == 'running':
            batman.state = 'idle'
    if keys[pygame.K_SPACE]:
        batman.jump()
    if keys[pygame.K_f]:
        batman.attack()

    if keys[pygame.K_a]:
        spider_man.x -= 5
        spider_man.state = 'running'
    elif keys[pygame.K_d]:
        spider_man.x += 5
        spider_man.state = 'running'
    else:
        if spider_man.state == 'running':
            spider_man.state = 'idle'
    if keys[pygame.K_z]:
        spider_man.jump()
    if keys[pygame.K_x]:
        spider_man.attack()

    # Обновление персонажей
    batman.update()
    spider_man.update()

    # Проверка столкновений
    if batman.is_attacking and batman.attack_rect and batman.attack_duration == 9:
        if batman.attack_rect.colliderect(spider_man.rect):
            spider_man.headpoints -= batman.strength
            print(f"{spider_man.name} получил удар от {batman.name}! HP: {spider_man.headpoints}")

    if spider_man.is_attacking and spider_man.attack_rect and spider_man.attack_duration == 9:
        if spider_man.attack_rect.colliderect(batman.rect):
            batman.headpoints -= spider_man.strength
            print(f"{batman.name} получил удар от {spider_man.name}! HP: {batman.headpoints}")

    # Отрисовка с учетом направления
    if batman.facing_right:
        batman_image = batman.image
    else:
        batman_image = pygame.transform.flip(batman.image, True, False)
    if spider_man.facing_right:
        spiderman_image = spider_man.image
    else:
        spiderman_image = pygame.transform.flip(spider_man.image, True, False)

    display.blit(batman_image, (batman.x, batman.y))
    display.blit(spiderman_image, (spider_man.x, spider_man.y))

    pygame.display.update()

pygame.quit()