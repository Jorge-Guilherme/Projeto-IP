import pygame as pg

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.Font(None, 74)
        self.small_font = pg.font.Font(None, 36)
        self.options = ["Iniciar Jogo", "Sair"]
        self.selected_option = 0

        # Carregar a imagem de fundo do menu
        self.background_image = pg.image.load('assets/screens/menu.png')
        self.background_image = pg.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))  # Desenhar a imagem de fundo

        title = self.font.render("Menu Principal", True, (255, 255, 255))
        self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 50))

        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.selected_option else (255, 255, 255)
            option_text = self.small_font.render(option, True, color)
            text_rect = option_text.get_rect(center=(self.screen.get_width() // 2, 150 + i * 50))
            self.screen.blit(option_text, text_rect)

            # Adiciona um retângulo ao redor da opção selecionada
            if i == self.selected_option:
                pg.draw.rect(self.screen, (255, 0, 0), text_rect.inflate(20, 10), 2)  # Adiciona uma borda vermelha

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pg.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pg.K_RETURN:
                return self.selected_option
        return None
