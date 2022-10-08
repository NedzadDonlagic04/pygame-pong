import pygame

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
        
        self.normalText = font.render(text, False, color)
        self.hoverText = font.render(text, False, 'White')

        self.image = self.normalText
        self.rect = self.image.get_rect( center = pos )

        self.hoverEffect = hoverEffect

        self.hoverSound = pygame.mixer.Sound('./audio/mouseHover.wav')
        self.soundPlayer = False
    
    def update(self):
        if self.hoverEffect:
            mouseX, mouseY = pygame.mouse.get_pos()

            if mouseX >= self.rect.left and mouseX <= self.rect.right and mouseY >= self.rect.top and mouseY <= self.rect.bottom:
                self.image = self.hoverText
                if not self.soundPlayer:
                    self.hoverSound.play()
                    self.soundPlayer = True
            else:
                self.image = self.normalText
                self.soundPlayer = False
