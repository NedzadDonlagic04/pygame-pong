import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        pygame.display.set_caption(title)
        
        self.screen = pygame.display.set_mode((width, height))

        self.clock = Clock(60)

        font = pygame.font.Font('./fonts/Pixeltype.ttf', 150)
        self.image1 = font.render('Pong', False, 'White')
        self.rect1 = self.image1.get_rect( center = (width / 2, 100))

        font = pygame.font.Font('./fonts/Pixeltype.ttf', 80)
        self.image2 = font.render('Play', False, 'Gray')
        self.rect2 = self.image2.get_rect( center = (width / 2, self.rect1.bottom + 70))

        font = pygame.font.Font('./fonts/Pixeltype.ttf', 80)
        self.image3 = font.render('Exit', False, 'Gray')
        self.rect3 = self.image3.get_rect( center = (width / 2, self.rect2.bottom + 50))

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

            self.startScreenText.update()
            self.startScreenText.draw(self.screen)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(600, 400, 'Pong')
    game.run()