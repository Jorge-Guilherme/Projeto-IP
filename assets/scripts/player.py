import pygame as pg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 200  # Tamanho visual do jogador
        self.collision_size = 50  # Tamanho da área de colisão reduzida
        self.velocity_y = 0
        self.on_ground = False
        self.health = 3
        self.animation_index = 0
        self.animation_speed = 0.2  # Ajuste a velocidade da animação conforme necessário
        self.heart_image = pg.image.load('assets/sprites/heart.png')
        self.heart_image = pg.transform.scale(self.heart_image, (30, 30))  # Ajuste o tamanho do coração conforme necessário
        self.sprites = self.load_sprites()
        self.jump_image = pg.image.load('assets/sprites/jump.png')  # Carrega a imagem de pulo
        self.jump_image = pg.transform.scale(self.jump_image, (self.size, self.size))  # Ajusta o tamanho da imagem de pulo
        self.rect = pg.Rect(self.x, self.y, self.collision_size, self.collision_size)  # Inicializa o retângulo de colisão
        self.direction = 1  # 1 para a direita, -1 para a esquerda

    def load_sprites(self):
        sprite_sheet = pg.image.load('assets/sprites/move.png').convert_alpha()
        sprite_width = sprite_sheet.get_width() // 10  # Dividindo por 10 quadros na largura
        sprite_height = sprite_sheet.get_height()
        sprites = []

        for i in range(10):
            rect = pg.Rect(i * sprite_width, 0, sprite_width, sprite_height)
            image = sprite_sheet.subsurface(rect)
            image = pg.transform.scale(image, (self.size, self.size))  # Redimensiona se necessário
            sprites.append(image)

        return sprites

    def update(self, keys, platforms, floor_y):
        # Atualiza a velocidade vertical (gravidade)
        self.velocity_y += 0.5
        self.y += self.velocity_y

        # Verifica a colisão com o piso
        if self.y + self.size > floor_y:
            self.y = floor_y - self.size
            self.velocity_y = 0
            self.on_ground = True

        # Verifica a colisão com plataformas (obstáculos)
        """
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Se está caindo
                    if self.y + self.size - self.velocity_y < platform.y:  # Checa se o jogador estava acima da plataforma
                        self.y = platform.y
                        self.velocity_y = 0
                        self.on_ground = True
                elif self.velocity_y < 0:  # Se está subindo
                    self.y = platform.y + platform.height
                    self.velocity_y = 0
        """
        # Movimentação horizontal
        if keys[pg.K_LEFT]:
            self.x -= 5
            self.animation_index += self.animation_speed
            self.direction = -1
        elif keys[pg.K_RIGHT]:
            self.x += 5
            self.animation_index += self.animation_speed
            self.direction = 1
        else:
            self.animation_index = 0

        # Pulo
        if keys[pg.K_UP] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False

        # Atualiza a posição do retângulo de colisão novamente após possíveis ajustes
        self.update_rect()

        # Mantém o índice da animação no intervalo correto
        if self.animation_index >= len(self.sprites):
            self.animation_index = 0

    def update_rect(self):
        # Ajusta a área de colisão para ser menor
        self.rect.topleft = (self.x + (self.size - self.collision_size) // 2, self.y + (self.size - self.collision_size) // 2)
        self.rect.size = (self.collision_size, self.collision_size)

    def draw(self, surface, camera):
        if not self.on_ground:  # Se não estiver no chão, desenha a imagem de pulo
            current_sprite = self.jump_image
        else:
            current_sprite = self.sprites[int(self.animation_index)]
        
        if self.direction == -1:
            current_sprite = pg.transform.flip(current_sprite, True, False)
        
        surface.blit(current_sprite, (self.x - camera.x, self.y - camera.y))

    def draw_health(self, surface):
        for i in range(self.health):
            surface.blit(self.heart_image, (10 + i * 40, 10))  # Ajuste a posição dos corações conforme necessário

    def add_health(self, amount):
        self.health = min(self.health + amount, 5)  # Limite máximo de 5 corações

    def remove_health(self, amount):
        self.health = max(self.health - amount, 0)  # Não permitir valores negativos
