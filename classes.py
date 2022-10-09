from curses import KEY_DOWN
import pygame
from random import randrange, choice

class Clock:
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self):
        self.clock.tick(self.FPS)

class Text(pygame.sprite.Sprite):
    def __init__(self, font_size, text, color, pos, hoverEffect=False):
        super().__init__()

        font = pygame.font.Font('./fonts/Pixeltype.ttf', font_size)
        
        self.text = text

        self.normalText = font.render(text, False, color)
        self.hoverText = font.render(text, False, 'White')

        self.image = self.normalText
        self.rect = self.image.get_rect( center = pos )

        self.hoverEffect = hoverEffect

        self.hoverSound = pygame.mixer.Sound('./audio/mouseHover.wav')
        self.soundPlayer = False
    
    def getText(self):
        return self.text

    def update(self):
        if self.hoverEffect:
            mouseX, mouseY = pygame.mouse.get_pos()

            if mouseX >= self.rect.left and mouseX <= self.rect.right and mouseY >= self.rect.top and mouseY <= self.rect.bottom:
                self.image = self.hoverText
                if not self.soundPlayer:
                    self.hoverSound.play()
                    self.soundPlayer = True
                if pygame.mouse.get_pressed()[0]:
                    return self.text

            else:
                self.image = self.normalText
                self.soundPlayer = False

class MouseEvent:
    def __init__(self):
        self.sprites = None
        self.text = None
    
    def detectClick(self, sprites):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            for sprite in sprites.sprites():
                if sprite.rect.collidepoint(pos):
                    self.text = sprite.getText()
                    return

class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        ball_img = pygame.Surface((15, 15), pygame.SRCALPHA)
        pygame.draw.circle(ball_img, (255, 255, 255), (7.5, 7.5), 7.5)
        self.image = ball_img

        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        self.directions = [-1 , 1]

    def setSpot(self, player=0):
        y = randrange(8, self.SCREEN_HEIGHT - 8, 1)
        self.rect = self.image.get_rect( center = (self.SCREEN_WIDTH/2, y))
        
        if player == 0:
            self.x = choice(self.directions)
        elif player == 1:
            self.x = -1
        else:
            self.x = 1

        self.y = choice(self.directions)

    def update(self, scores):
        self.rect.top += self.y
        self.rect.left += self.x

        if self.rect.top == 0 or self.rect.bottom == self.SCREEN_HEIGHT:
            self.y = -self.y
        if self.rect.left == 0 or self.rect.right == self.SCREEN_WIDTH:
            if self.rect.left == 0:
                scores.scoreUpdate(2)
                self.setSpot(2)
            else:
                scores.scoreUpdate(1)
                self.setSpot(1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
class Border(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load('./img/border.png').convert_alpha()
        self.rect = self.image.get_rect( center = (width/2, height/2)) 

class Scores:
    def __init__(self, width, font_size):
        self.font = pygame.font.Font('./fonts/Pixeltype.ttf', font_size)

        self.scoreReset()

        self.rect1 = self.image1.get_rect( center = (width/4, 50))
        self.rect2 = self.image2.get_rect( center = (3*width/4, 50))

    def scoreReset(self):
        self.score1 = 0
        self.score2 = 0

        self.image1 = self.font.render(str(self.score1), False, 'White')
        self.image2 = self.font.render(str(self.score2), False, 'White')

    def getScores(self):
        return (self.score1, self.score2)

    def scoreUpdate(self, side):
        if side == 1:
            self.score1 += 1
            self.image1 = self.font.render(str(self.score1), False, 'White')
        else:
            self.score2 += 1
            self.image2 = self.font.render(str(self.score2), False, 'White')

    def draw(self, screen, state):
        screen.blit(self.image1, self.rect1)
        screen.blit(self.image2, self.rect2)

        if self.getScores()[0] == 3 or self.getScores()[1] == 3:
            return state
    
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, player):
        super().__init__()

        self.image = pygame.image.load('./img/player.png').convert_alpha()
        
        if player == 1:
            self.rect = self.image.get_rect( center = (width/8, height/2) )
        else:
            self.rect = self.image.get_rect( center = (7*width/8, height/2) )

        self.player = player
        self.WIDTH = width
        self.HEIGHT = height

        self.speed = 3
    
    def update(self):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            if keys[pygame.K_w]:
                if self.rect.top < 0:
                    self.rect.top = 0
                else:
                    self.rect.top -= self.speed
            elif keys[pygame.K_s]:
                if self.rect.bottom > self.HEIGHT:
                    self.rect.bottom = self.HEIGHT
                else:
                    self.rect.bottom += self.speed
        else:
            if keys[pygame.K_UP]:
                if self.rect.top < 0:
                    self.rect.top = 0
                else:
                    self.rect.top -= self.speed
            elif keys[pygame.K_DOWN]:
                if self.rect.bottom > self.HEIGHT:
                    self.rect.bottom = self.HEIGHT
                else:
                    self.rect.bottom += self.speed
