import pygame as pg

# Resolução da janela
resolA = 1280
resolL = 720

pg.init()

game_window = pg.display.set_mode([resolA, resolL])
pg.display.set_caption("SilasPilgrimVSTheCIn")

block_color = (0, 100, 255)

block_size = 50

# Info do bloco (Spawn e speed)
block_x = resolA // 2
block_y = resolL // 2

block_speed = 2

# Loop do jogo
gameloop = True
while gameloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            gameloop = False

    # Obtendo as teclas pressionadas
    keys = pg.key.get_pressed()

    # Movendo o bloco de acordo com as teclas pressionadas
    if keys[pg.K_LEFT]:
        block_x -= block_speed
    if keys[pg.K_RIGHT]:
        block_x += block_speed
    if keys[pg.K_UP]:
        block_y -= block_speed
    if keys[pg.K_DOWN]:
        block_y += block_speed

    # Preenchendo a tela com uma cor (preto)
    game_window.fill((0, 0, 0))

    # Desenhando o bloco na nova posição
    pg.draw.rect(game_window, block_color, (block_x, block_y, block_size, block_size))

    # Atualizando a tela
    pg.display.update()
