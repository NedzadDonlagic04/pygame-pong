import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        pygame.display.set_caption(title)
        
        self.screen = pygame.display.set_mode((width, height))

        self.clock = Clock(60)

        self.WIDTH = width
        self.HEIGHT = height

        icon = pygame.image.load('./img/pong-icon.png').convert_alpha()
        pygame.display.set_icon(icon)
        
        pongText = Text(150, 'Pong', 'White', (width / 2, 100))
        startText = Text(80, 'Play', 'Gray', (width / 2, pongText.rect.bottom + 70), True)
        exitText = Text(80, 'Exit', 'Gray', (width / 2, startText.rect.bottom + 50), True)

        self.startScreenText = pygame.sprite.Group(pongText, startText, exitText)

    def closeGame(self):
        pygame.quit()
        exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.closeGame()

            pygame.draw.rect(self.screen, 'Black', (0, 0, self.WIDTH, self.HEIGHT))

            self.startScreenText.update()
            self.startScreenText.draw(self.screen)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(600, 400, 'Pong')
    game.run()