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

    def setSpot(self):
        y = randrange(8, self.SCREEN_HEIGHT - 8, 1)
        self.rect = self.image.get_rect( center = (self.SCREEN_WIDTH/2, y))
        
        self.x = choice(self.directions)
        self.y = choice(self.directions)

    def update(self):
        self.rect.top += self.y
        self.rect.left += self.x

        if self.rect.top == 0 or self.rect.bottom == self.SCREEN_HEIGHT:
            self.y = -self.y
        if self.rect.left == 0 or self.rect.right == self.SCREEN_WIDTH:
            self.x = -self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)


