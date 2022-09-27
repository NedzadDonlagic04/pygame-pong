import pygame
from sys import exit

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

    def closeGame(self):
        pygame.quit()
        exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.closeGame()

            pygame.display.update()

if __name__ == '__main__':
    game = Game(600, 400, 'Pong')
    game.run()