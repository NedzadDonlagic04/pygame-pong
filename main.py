import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        pygame.display.set_caption(title)
        
        self.screen = pygame.display.set_mode((width, height))

        self.clock = Clock(60)

    def closeGame(self):
        pygame.quit()
        exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.closeGame()

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(600, 400, 'Pong')
    game.run()