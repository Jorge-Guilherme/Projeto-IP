import pygame as pg

class Item:
    def __init__(self, x, y, name, rare, description, hp, damage):
        self.x = x
        self.y = y
        self.size = 200
        self.name = name
        self.rare = rare
        self.description = description
        self.hp = hp
        self.damage = damage
        self.image = None
        self.collision_width = self.size // 2
        self.collision_height = self.size // 2
        self.rect = pg.Rect(self.x, self.y, 50, 50)  # Área de colisão

    def set_collision_size(self, width, height):
        self.collision_width = 50
        self.collision_height = 50
        self.update_rect()

    def update_rect(self):
        # Centraliza a área de colisão na posição atual
        self.rect = pg.Rect(
            self.x + 70,
            self.y + 40,
            50,
            50
        )

    def draw(self, surface, camera):
        item_rect = pg.Rect(self.x - camera.x, self.y - camera.y, self.size, self.size)
        if self.image:
            surface.blit(self.image, item_rect)
        else:
            pg.draw.rect(surface, self.color, item_rect)

class Collectible(Item):
    def __init__(self, x, y, name, rare, description):
        super().__init__(x, y, name, rare, description, hp=description, damage=0)
        self.color = (255, 255, 0)  # Amarelo para coletáveis
        self.image = pg.image.load(f"assets/sprites/powerups/{name.lower()}.png")
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        # Atualiza a área de colisão
        self.set_collision_size(self.size // 2, self.size // 2)

class Enemy(Item):
    def __init__(self, x, y, name, rare, description, hp, damage, move_range=0, speed=0):
        super().__init__(x, y, name, rare, description, hp, damage)
        self.color = (255, 0, 0)
        self.image = pg.image.load(f"assets/sprites/enemys/{name.lower()}.png")
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.initial_x = x
        self.move_range = move_range
        self.speed = speed
        self.direction = 1
        # Atualiza a área de colisão
        self.set_collision_size(self.size // 2, self.size // 2)

    def update(self):
        if self.move_range > 0:
            self.x += self.speed * self.direction
            if self.x <= self.initial_x - self.move_range or self.x >= self.initial_x + self.move_range:
                self.direction *= -1
        self.update_rect()

    def draw(self, surface, camera):
        surface.blit(self.image, (self.x - camera.x, self.y - camera.y))

class AnimatedEnemy(Enemy):
    def __init__(self, x, y, name, rare, description, hp, damage, move_range=200, speed=2):
        super().__init__(x, y, name, rare, description, hp, damage, move_range, speed)
        self.animation_index = 0
        self.animation_speed = 0.3  # Ajuste a velocidade da animação conforme necessário
        self.sprites = self.load_sprites()

    def load_sprites(self):
        sprite_sheet = pg.image.load(f'assets/sprites/enemys/{self.name.lower()}.png').convert_alpha()
        sprite_width = sprite_sheet.get_width() // 5  # Suponha 5 sprites na largura
        sprite_height = sprite_sheet.get_height()  # Suponha 1 linha de sprites
        sprites = []

        for i in range(5):  # Número de quadros na animação
            rect = pg.Rect(i * sprite_width, 0, sprite_width, sprite_height)
            image = sprite_sheet.subsurface(rect)
            image = pg.transform.scale(image, (self.size, self.size))
            sprites.append(image)

        return sprites

    def update(self):
        super().update()
        # Atualizar a animação
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.sprites):
            self.animation_index = 0

    def draw(self, surface, camera):
        current_sprite = self.sprites[int(self.animation_index)]
        if self.direction == -1:
            current_sprite = pg.transform.flip(current_sprite, True, False)
        surface.blit(current_sprite, (self.x - camera.x, self.y - camera.y))
