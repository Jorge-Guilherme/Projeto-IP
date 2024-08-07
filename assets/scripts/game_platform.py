import pygame as pg

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (200, 0, 0)  # Cor vermelha para a plataforma
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, camera):
        # Ajusta a posição da plataforma de acordo com a câmera
        platform_rect = self.rect.move(-camera.x, -camera.y)
        pg.draw.rect(surface, self.color, platform_rect)

    def update_rect(self):
        # Atualiza o retângulo de colisão
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
