class Character:
    def __init__(self, name, headpoints, x, y, image, strength, sprites: list):
        self.name = name
        self.headpoints = headpoints
        self.x = x
        self.y = y
        self.image = image
        self.strength = strength
        self.speed = 0.5
        self.sprites = sprites
