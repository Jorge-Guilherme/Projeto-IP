import pygame as pg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.speed = 5
        self.jump_height = 12
        self.gravity = 0.5
        self.velocity_y = 0
        self.on_ground = False
        self.jump_delay = 1200  # Em milissegundos
        self.last_jump_time = 0
        self.color = (0, 100, 255)
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)
        self.on_platform = False

    def update(self, keys, platforms, floor_y):
        # Movendo o jogador
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.x += self.speed
        if keys[pg.K_UP] and (self.on_ground or pg.time.get_ticks() - self.last_jump_time > self.jump_delay):
            if self.on_ground:
                self.velocity_y = -self.jump_height
                self.on_ground = False
                self.last_jump_time = pg.time.get_ticks()  # Atualiza o tempo do último pulo
            elif not self.on_ground and pg.time.get_ticks() - self.last_jump_time > self.jump_delay:
                self.velocity_y = -self.jump_height
                self.last_jump_time = pg.time.get_ticks()  # Atualiza o tempo do último pulo

        # Aplicando gravidade
        self.y += self.velocity_y
        self.velocity_y += self.gravity

        # Verificando colisão com o chão
        if self.y + self.size > floor_y:
            self.y = floor_y - self.size
            self.velocity_y = 0
            self.on_ground = True

        # Verificando colisão com as plataformas
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)
        self.on_ground = False  # Presume que não está no chão até que uma colisão seja detectada
        self.on_platform = False  # Presume que não está em uma plataforma até que uma colisão seja detectada
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Colisão pelo topo da plataforma
                if self.velocity_y > 0 and self.y + self.size - self.velocity_y <= platform.y:
                    self.y = platform.y - self.size
                    self.velocity_y = 0
                    self.on_ground = True
                    self.on_platform = True
                # Colisão pela lateral esquerda
                elif self.x + self.size > platform.x and self.x < platform.x and self.y + self.size > platform.y:
                    self.x = platform.x - self.size
                # Colisão pela lateral direita
                elif self.x < platform.x + platform.width and self.x + self.size > platform.x + platform.width and self.y + self.size > platform.y:
                    self.x = platform.x + platform.width

        # Verifica se o bloco está no chão verde ou em alguma plataforma
        if not self.on_ground:
            if self.y + self.size > floor_y:
                self.y = floor_y - self.size
                self.velocity_y = 0
                self.on_ground = True

        # Verifica se a seta para baixo é pressionada e o bloco está em uma plataforma
        if keys[pg.K_DOWN] and self.on_platform:
            self.y += self.size
            self.on_ground = False
            self.on_platform = False  # Deixar de estar em cima da plataforma

    def draw(self, surface, camera):
        # Ajusta a posição do jogador de acordo com a câmera
        player_rect = pg.Rect(self.x - camera.x, self.y - camera.y, self.size, self.size)
        pg.draw.rect(surface, self.color, player_rect)
