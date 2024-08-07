import pygame as pg

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (128, 128, 128)  # Cor cinza para os obstáculos
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, camera):
        # Ajusta a posição do obstáculo de acordo com a câmera
        obstacle_rect = self.rect.move(-camera.x, -camera.y)
        pg.draw.rect(surface, self.color, obstacle_rect)

    def update_rect(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

