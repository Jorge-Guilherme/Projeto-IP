import pygame as pg
from assets.scripts.player import Player
from assets.scripts.collectibles import Collectible, Enemy, AnimatedEnemy
from assets.scripts.obstacles import Obstacle
from assets.scripts.menu import Menu

# Inicialização do Pygame
pg.init()

# Resolução da janela
resolA = 1280
resolL = 720

game_window = pg.display.set_mode([resolA, resolL])
pg.display.set_caption("SilasPilgrimVSTheCIn")

# Carregar a imagem do cenário do mapa
background_image = pg.image.load(r"assets/sprites/paralax/bg.png")

# Carregar a imagem de game over
game_over_image = pg.image.load(r"assets/screens/bg_gameover.png")

# Redimensionar a imagem do cenário do mapa
new_height = 720
scale_factor = new_height / background_image.get_height()
new_width = int(background_image.get_width() * scale_factor)
background_image = pg.transform.scale(background_image, (new_width, new_height))

# Dimensões do mapa baseadas na imagem redimensionada
map_width, map_height = background_image.get_size()

# Cores
background_color = (0, 0, 0)
floor_color = (0, 255, 0)
collision_color = (255, 0, 0, 128)  # Vermelho semitransparente para a área de colisão

# Coletáveis (Distância para o início, Altura)
collectibles_data = [
    (2800, 500, "pg", 0, 1), # segundo coletável
    (300, 500, "heroi_diferente", 1, 1), # primeiro coletável
    (3300, 300, "bocudo", 3, 1),
    (4100, 450, "renata", 4, 1),
    (4400, 450, "sofia", 7, 1),
    (4900, 400, "kab_esticada", 1, 1),
]

def create_collectibles():
    return [Collectible(*data) for data in collectibles_data]

collectibles = create_collectibles()

# Inimigos (Distância para o início, Altura)
enemies_data = [
    (1300, 350, "greve", 2, "VOU FAZER A CHAMADA!", 1, 1), # primeiro desafio
    (1300, 250, "greve", 2, "VOU FAZER A CHAMADA!", 1, 1),
    (1300, 150, "greve", 2, "VOU FAZER A CHAMADA!", 1, 1),
    (1300, 450, "greve", 2, "VOU FAZER A CHAMADA!", 1, 1),
    (1300, 550, "greve", 2, "VOU FAZER A CHAMADA!", 1, 1),
    (3500, 480, "greve", 2, "VOU FAZER A CHAMADA!", 1, 1),
    (2500, 480, "ru_fechado", 5, "TERMINOU A LISTA?", 1, 1), 
    (3200, 480, "ru_fechado", 5, "TERMINOU A LISTA?", 1, 1),
    (3800, 480, "greve", 8, "NÃO ME CHAME DE PROFESSOR!", 3, 2),
    (4300, 500, "ricardo", 3, "Eu me movo!", 1, 1, 300, 3),
    (1000, 500, "gusto", 3, "Eu me movo!", 1, 1, 300, 3), # primeiro desafio
    (4600, 500, "ru_fechado", 5, "TERMINOU A LISTA?", 1, 1),
    (4600, 350, "ru_fechado", 5, "TERMINOU A LISTA?", 1, 1)
]

# Dados dos obstáculos: (x, y, largura, altura)
obstacles_data = [
    (600, 500, 100, 20), # primeira fase
    (800, 350, 100, 20),
    (1000, 250, 300, 20),

    (2600, 450, 250, 20), # segunda fase
    (3000, 450, 250, 20),

    (3300, 400, 100, 20), # terceira fase
    (3600, 300, 200, 20),
    (4000, 450, 150, 20),
    (4400, 300, 250, 20),
    (4700, 300, 100, 20)

]

def create_enemies():
    enemies = []
    for data in enemies_data:
        if len(data) > 7:  # Se move_range e speed estiverem definidos, crie um AnimatedEnemy
            enemies.append(AnimatedEnemy(*data))
        else:
            enemies.append(Enemy(*data))
    return enemies

enemies = create_enemies()

# Ordenando os itens pela raridade
collectibles.sort(key=lambda item: item.rare)
enemies.sort(key=lambda item: item.rare)

# Criação de objetos
player = Player(100, 100)

# Configuração da câmera
camera = pg.Rect(0, 0, resolA, resolL)

# Configuração do piso
floor_height = 20
floor_y = map_height - floor_height

# Criação dos objetos Obstáculo
obstacles = [Obstacle(*data) for data in obstacles_data]

def restart_game():
    global collectibles, enemies
    player.x = 100
    player.y = 100
    player.velocity_y = 0
    player.on_ground = False
    player.health = 3
    player.update_rect()
    collectibles = create_collectibles()
    enemies = create_enemies()

def draw_map_background():
    game_window.blit(background_image, (-camera.x, -camera.y))

def draw_game_over():
    game_window.blit(game_over_image, (resolA // 2 - game_over_image.get_width() // 2, resolL // 2 - game_over_image.get_height() // 2))
    pg.display.update()

def game_over():
    draw_game_over()
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:  # Pressione Enter para reiniciar
                    restart_game()
                    waiting = False

def show_main_menu():
    menu = Menu(game_window)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            result = menu.handle_events(event)
            if result is not None:
                return result
        
        menu.draw()
        pg.display.update()

def you_win():
    font = pg.font.Font(None, 74)
    text = font.render("You Win!", True, (255, 255, 255))
    game_window.blit(text, (resolA // 2 - text.get_width() // 2, resolL // 2 - text.get_height() // 2))
    pg.display.update()
    pg.time.wait(3000)  # Espera 3 segundos
    restart_game()  # Reinicia o jogo após ganhar


# Loop principal
def main():
    while True:
        choice = show_main_menu()
        if choice == 0:  # Iniciar Jogo
            gameloop = True
            clock = pg.time.Clock()
            while gameloop:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        gameloop = False

                # Atualizando o jogador
                keys = pg.key.get_pressed()
                player.update(keys, obstacles, floor_y)

                # Verifica se o jogador caiu no piso mortal
                if player.y + player.size > floor_y + floor_height:
                    player.remove_health(1)  # Remove um coração ao cair
                    if player.health <= 0:
                        game_over()
                        continue

                # Atualiza a posição da câmera para seguir o jogador
                camera.center = (player.x + player.size // 2, player.y + player.size // 2)

                # Restringe a câmera dentro dos limites do mapa
                if camera.left < 0:
                    camera.left = 0
                if camera.right > map_width:
                    camera.right = map_width
                if camera.top < 0:
                    camera.top = 0
                if camera.bottom > map_height:
                    camera.bottom = map_height

                # Desenhando o cenário do mapa
                draw_map_background()

                # Desenhando o piso verde
                floor_rect = pg.Rect(-camera.x, floor_y - camera.y, map_width, floor_height)
                pg.draw.rect(game_window, floor_color, floor_rect)

                # Desenhando os obstáculos e os canos
                for obstacle in obstacles:
                    obstacle.draw(game_window, camera)

                # Atualização e desenho dos inimigos
                for enemy in enemies:
                    enemy.update()  # Atualiza a posição e a animação do inimigo, se aplicável
                    enemy.draw(game_window, camera)
                    if player.rect.colliderect(enemy.rect):
                        player.remove_health(enemy.damage)  # Remove a saúde com base no dano do inimigo
                        enemies.remove(enemy)
                        if player.health <= 0:
                            game_over()
                            continue

                # Verifica colisão do jogador com obstáculos
                player_rect = player.rect.copy()
                player_rect.x -= camera.x
                player_rect.y -= camera.y

                for obstacle in obstacles:
                    obstacle_rect = obstacle.rect.copy()
                    obstacle_rect.x -= camera.x
                    obstacle_rect.y -= camera.y
                    if player_rect.colliderect(obstacle_rect):
                        if player.y != 500 and player.velocity_y > 0:  # Colisão de baixo para cima
                            player.y = (obstacle.y - (player.size // 2)) - 26
                            player.velocity_y = 0
                            player.on_ground = True
                            
                        #elif player.velocity_y < 0 and not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):  # Colisão de cima para baixo
                            #player.y = obstacle.y + obstacle.height
                            #player.velocity_y = 0
                        
                            # Ajusta a posição horizontal do jogador
                            """
                            if player_rect.right > obstacle_rect.left and player_rect.left < obstacle_rect.right:
                                if player.x < obstacle.x:
                                    player.x = (obstacle.x - (player.size // 2))
                                else:
                                    player.x = obstacle.x + obstacle.width
                            """
                        
                    # Atualiza a área de colisão do obstáculo se necessário
                    obstacle.update_rect()

                # Atualizando e desenhando os coletáveis
                for collectible in collectibles:
                    collectible.draw(game_window, camera)
                    if player.rect.colliderect(collectible.rect):
                        collectibles.remove(collectible)
                        if collectible.name == "kab_esticada":
                            you_win()
                        else:
                            player.add_health(1)  # Adiciona um coração ao pegar um coletável


                # Desenhando o jogador
                player.draw(game_window, camera)

                # Desenhando a área de colisão
                #pg.draw.rect(game_window, collision_color, player.rect.move(-camera.x, -camera.y), 2)
                #for enemy in enemies:
                    #pg.draw.rect(game_window, collision_color, enemy.rect.move(-camera.x, -camera.y), 2)
                #for collectible in collectibles:
                    #pg.draw.rect(game_window, collision_color, collectible.rect.move(-camera.x, -camera.y), 2)
                #for obstacle in obstacles:
                    #pg.draw.rect(game_window, collision_color, obstacle.rect.move(-camera.x, -camera.y), 2)

                # Desenhando a vida do jogador
                player.draw_health(game_window)

                # Atualizando a tela
                pg.display.update()

                # Controlando a taxa de quadros por segundo (FPS)
                clock.tick(60)
        
        elif choice == 1:  # Sair
            pg.quit()
            exit()

if __name__ == "__main__":
    main()
