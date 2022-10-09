import pygame
from sys import exit
from classes import *

class Game:
    MAIN_MENU = 0
    GAME_ONGOING = 1
    PAUSE = 2

    def __init__(self, width, height, title):
        pygame.init()

        pygame.display.set_caption(title)
        
        self.screen = pygame.display.set_mode((width, height))

        self.clock = Clock(60)

        self.WIDTH = width
        self.HEIGHT = height

        icon = pygame.image.load('./img/pong-icon.png').convert_alpha()
        pygame.display.set_icon(icon)
        
        self.pongText = Text(150, 'Pong', 'White', (width / 2, 100))
        self.startText = Text(80, 'Play', 'Gray', (width / 2, self.pongText.rect.bottom + 70), True)
        self.exitText = Text(80, 'Exit', 'Gray', (width / 2, self.startText.rect.bottom + 50), True)

        self.pauseText = Text(150, 'Pause', 'White', (width / 2, 100))
        self.continueText = Text(80, 'Continue', 'Gray', (width / 2, self.pauseText.rect.bottom + 50), True)
        self.mainMenuText = Text(80, 'Main Menu', 'Gray', (width / 2, self.continueText.rect.bottom + 70), True)

        self.mouse = MouseEvent()

        self.ball = Ball(width, height)
        self.border = pygame.sprite.GroupSingle( Border(width, height) )

        self.onScreenText = pygame.sprite.Group(self.pongText, self.startText, self.exitText)
        self.state = self.MAIN_MENU

    def closeGame(self):
        pygame.quit()
        exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.mouse.text == 'Exit':
                    self.closeGame()
                elif self.mouse.text == 'Play':
                    self.mouse.text = None
                    self.state = self.GAME_ONGOING
                    self.ball.setSpot()
                elif event.type == pygame.KEYDOWN:
                    if self.state == self.GAME_ONGOING and event.key == pygame.K_ESCAPE:
                        self.state = self.PAUSE
                        self.onScreenText = pygame.sprite.Group(self.pauseText, self.continueText, self.mainMenuText)
                elif self.mouse.text == 'Main Menu':
                    self.state = self.MAIN_MENU
                    self.onScreenText = pygame.sprite.Group(self.pongText, self.startText, self.exitText)
                elif self.mouse.text == 'Continue':
                    self.state = self.GAME_ONGOING
                    self.mouse.text = None

            pygame.draw.rect(self.screen, 'Black', (0, 0, self.WIDTH, self.HEIGHT))

            if self.state == self.MAIN_MENU:
                self.onScreenText.update()
                self.onScreenText.draw(self.screen)
                self.mouse.detectClick(self.onScreenText)
            elif self.state == self.GAME_ONGOING:
                self.border.draw(self.screen)
                
                self.ball.update()
                self.ball.draw(self.screen)
            elif self.state == self.PAUSE:
                self.onScreenText.update()
                self.onScreenText.draw(self.screen)
                self.mouse.detectClick(self.onScreenText)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(600, 400, 'Pong')
    game.run()