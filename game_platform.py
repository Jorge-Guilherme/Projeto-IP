import pygame as pg

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (200, 0, 0)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, camera):
        # Ajusta a posição da plataforma de acordo com a câmera
        platform_rect = pg.Rect(self.x - camera.x, self.y - camera.y, self.width, self.height)
        pg.draw.rect(surface, self.color, platform_rect)
