import pygame
from character import Character

pygame.init()
width = 1000
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fight Club")
background = pygame.image.load('assets/images/background.jpg')

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

# Функция для отображения здоровья в углах
def draw_health_bar_corner(character, surface, position):
    bar_width = 200
    bar_height = 20
    if position == 'left':
        bar_x = 20
    else:
        bar_x = width - bar_width - 20
    bar_y = 20
    hp_ratio = character.headpoints / 100

    if hp_ratio > 0.6:
        color = (0, 255, 0)
    elif hp_ratio > 0.3:
        color = (255, 255, 0)
    else:
        color = (255, 0, 0)

    pygame.draw.rect(surface, (0, 0, 0), (bar_x - 2, bar_y - 2, bar_width + 4, bar_height + 4))
    pygame.draw.rect(surface, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(surface, color, (bar_x, bar_y, bar_width * hp_ratio, bar_height))

    font = pygame.font.SysFont('Arial', 20)
    name_surface = font.render(character.name, True, (255, 255, 255))
    surface.blit(name_surface, (bar_x, bar_y + bar_height + 5))

exit = False
clock = pygame.time.Clock()

while not exit:
    clock.tick(40)
    display.blit(background, (0, 0))
    # pygame.draw.rect(display, (255, 255, 255), pygame.Rect(200, 200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

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

    batman.update()
    spider_man.update()

    if batman.is_attacking and batman.attack_rect and batman.attack_duration == 9:
        if batman.attack_rect.colliderect(spider_man.rect):
            spider_man.headpoints -= batman.strength
            print(f"{spider_man.name} получил удар от {batman.name}! HP: {spider_man.headpoints}")

    if spider_man.is_attacking and spider_man.attack_rect and spider_man.attack_duration == 9:
        if spider_man.attack_rect.colliderect(batman.rect):
            batman.headpoints -= spider_man.strength
            print(f"{batman.name} получил удар от {spider_man.name}! HP: {batman.headpoints}")

    batman_image = batman.image if batman.facing_right else pygame.transform.flip(batman.image, True, False)
    spiderman_image = spider_man.image if spider_man.facing_right else pygame.transform.flip(spider_man.image, True, False)

    display.blit(batman_image, (batman.x, batman.y))
    display.blit(spiderman_image, (spider_man.x, spider_man.y))

    draw_health_bar_corner(batman, display, 'left')
    draw_health_bar_corner(spider_man, display, 'right')

    pygame.display.update()

pygame.quit()