import pygame as pg
from player import Player
from game_platform import Platform

# Inicialização do Pygame
pg.init()

# Resolução da janela
resolA = 1280
resolL = 720

game_window = pg.display.set_mode([resolA, resolL])
pg.display.set_caption("SilasPilgrimVSTheCIn")

# Cores
background_color = (0, 0, 0)
floor_color = (0, 255, 0)  # Cor verde para o piso
death_color = (255, 0, 0)  # Cor vermelha para o piso mortal

# Background
background_image = pg.image.load('assets/cin.jpeg')
background_image = pg.transform.scale(background_image, (resolA, resolL))


# Info das plataformas
platforms = [
    (200, 600, 200, 20),  # (x, y, width, height)
    (500, 450, 200, 20),
    (800, 300, 200, 20),
]

# Criação de objetos
player = Player(resolA // 2, resolL // 2)
platform_objects = [Platform(*p) for p in platforms]

# Configuração da câmera
camera = pg.Rect(0, 0, resolA, resolL)

# Configuração do piso
floor_height = 20  # Altura do piso verde
floor_y = resolL - floor_height
death_height = 20  # Altura do piso mortal
death_y = floor_y + death_height

# Função para reiniciar o jogo
def restart_game():
    player.x = resolA // 2
    player.y = resolL // 2
    player.velocity_y = 0
    player.on_ground = False

# Loop do jogo
gameloop = True
clock = pg.time.Clock()
while gameloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            gameloop = False

    # Atualizando o jogador e plataformas
    keys = pg.key.get_pressed()
    player.update(keys, platform_objects, floor_y)

    # Verifica se o jogador caiu no piso mortal
    if player.y + player.size > death_y:
        restart_game()

    # Atualiza a posição da câmera para seguir o jogador
    camera.center = (player.x + player.size // 2, player.y + player.size // 2)

    # Preenchendo a tela com uma cor (preto)
    game_window.fill(background_color)

    # Desenhando o fundo
    game_window.blit(background_image, (0, 0))

    # Desenhando o piso verde
    floor_rect = pg.Rect(-camera.x, floor_y - camera.y, resolA * 2, floor_height)
    pg.draw.rect(game_window, floor_color, floor_rect)

    # Desenhando o piso mortal
    death_rect = pg.Rect(-camera.x, death_y - camera.y, resolA * 2, death_height)
    pg.draw.rect(game_window, death_color, death_rect)

    # Desenhando o jogador
    player.draw(game_window, camera)

    # Desenhando as plataformas
    for platform in platform_objects:
        platform.draw(game_window, camera)

    # Atualizando a tela
    pg.display.update()
    clock.tick(60)  # Limita o loop para rodar a 60 quadros por segundo (fps)
