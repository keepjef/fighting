import pygame
import math


class Character:
    def __init__(self, name, headpoints, x, y, image, strength, sprites: list, attack_sprites: list, jump_sprites: list):
        self.name = name
        self.headpoints = headpoints
        self.x = x
        self.y = y
        self.image = image  # Текущее изображение
        self.strength = strength
        self.speed = 0.5
        self.sprites = sprites  # Список спрайтов для бега
        self.attack_sprites = attack_sprites  # Список спрайтов для атаки
        self.jump_sprites = jump_sprites  # Список спрайтов для прыжка
        self.rect = pygame.Rect(x, y, 50, 50)  # Хитбокс персонажа
        self.state = 'idle'  # Текущее состояние: 'idle', 'running', 'attacking', 'jumping'
        self.current_sprite = 0  # Текущий кадр анимации
        self.animation_speed = 0.2  # Скорость анимации
        self.is_attacking = False  # Флаг атаки
        self.attack_rect = None  # Хитбокс атаки
        self.attack_duration = 0  # Длительность атаки (в кадрах)

        # Переменныеt для прыжка
        self.on_ground = True
        self.jump_height_flag = False
        self.velocity = 0
        self.a = 0
        self.jump_height = 0

        # Направление персонажа
        self.facing_right = True  # True - смотрит вправо, False - влево
        self.previous_x = x  # Предыдущая позиция для отслеживания движения

    def jump(self):
        """Инициирует прыжок, если персонаж на земле"""
        if self.on_ground:
            self.state = 'jumping'
            self.current_sprite = 0
            self.jump_height_flag = True
            self.jump_height = self.y - 150  # Высота прыжка
            self.velocity = 5  # Начальная скорость
            self.a = 25  # Ускорение
            self.on_ground = False

    def attack(self):
        """Запуск атаки"""
        if not self.is_attacking:
            self.state = 'attacking'
            self.current_sprite = 0
            self.is_attacking = True
            self.attack_duration = 10  # Атака длится 10 кадров
            attack_range = 150  # расстояние удара по оси X

            if self.facing_right:
                self.attack_rect = pygame.Rect(self.x + attack_range, self.y, 50, 50)  # Вправо
            else:
                self.attack_rect = pygame.Rect(self.x - attack_range, self.y, 50, 50)
    def update(self):
        """Обновление состояния, анимации и позиции персонажа"""
        # Обновление направления
        if self.x < self.previous_x:
            self.facing_right = False
        elif self.x > self.previous_x:
            self.facing_right = True
        self.previous_x = self.x

        # Обновление хитбокса
        self.rect.topleft = (self.x, self.y)

        # Логика прыжка
        if not self.on_ground and self.jump_height_flag:
            self.velocity += math.sqrt(self.a)
            self.y -= self.velocity
            if self.y <= self.jump_height:
                self.velocity = 0
                self.a = 0.6
                self.jump_height_flag = False
        elif not self.on_ground:
            self.y += self.velocity
            self.velocity += self.a ** 2
            if self.y >= 200:  # Уровень земли
                self.y = 200
                self.on_ground = True
                self.state = 'idle'

        # Анимация в зависимости от состояния
        if self.state == 'running':
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
        elif self.state == 'attacking':
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.attack_sprites):
                self.current_sprite = 0
                self.state = 'idle'
                self.is_attacking = False
                self.attack_rect = None
            else:
                self.image = self.attack_sprites[int(self.current_sprite)]
            if self.is_attacking:
                self.attack_duration -= 1
                if self.attack_duration <= 0:
                    self.state = 'idle'
                    self.is_attacking = False
                    self.attack_rect = None
        elif self.state == 'jumping':
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.jump_sprites):
                self.current_sprite = len(self.jump_sprites) - 1  # Останавливаемся на последнем кадре
            self.image = self.jump_sprites[int(self.current_sprite)]
        else:  # idle
            self.image = self.sprites[0]