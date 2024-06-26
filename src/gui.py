import pygame
from pygame.time import get_ticks

class Button:
    def __init__(self, x, y, img, hoverImg) -> None:
        self.img = img
        self.hoverImg = hoverImg
        self.currentImg = None
        self.button = self.img.get_rect()
        self.button.topleft = (x, y)
        self.clicked = False

        self.disabled = False

    # def fix(self, screen):
    #     pygame.draw.rect(screen, (110, 110, 110), self.button)
    #     screen.blit(self.img, (self.button.x + 5, self.button.y + 5))

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.button.collidepoint(pos) and not self.disabled:
            self.currentImg = self.hoverImg
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        else:
            self.currentImg = self.img
        surface.blit(self.currentImg, (self.button.x, self.button.y))
        return action

    def render(self):
        # Turns the pet class into a pygame surface so it can be displayed
        # Create a surface with the specified width and height
        pet_surface = pygame.Surface((self.img.get_width(),self.img.get_height())).convert_alpha()
        # Fill the surface with the color of the pet
        pet_surface.fill((0,0,0,0))
        # Assuming image is a pygame.Surface representing the appearance of the pet
        # You can blit the image onto the surface, adjust the position as needed
        pet_surface.blit(self.img, (0, 0))  # Assuming the image starts at position (0, 0) on the surface
        return pet_surface  


class HealthBar:
    def __init__(self, x, y, width, height, maxHP, healthColor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = maxHP
        self.maxHP = maxHP
        self.color = healthColor

    def draw(self, screen):
        #calculate the health ratio
        ratio = self.hp / self.maxHP
        
        pygame.draw.rect(screen, 'red', (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width * ratio, self.height))


class Label:
    def __init__(self, txt,  fontColor, fontSize, bold, x, y) -> None:
        self.txt = txt
        self.fontColor = fontColor
        self.fontSize = fontSize
        self.bold = bold
        self.x = x
        self.y = y
        self.width = 0

    def draw(self, screen):
        font = pygame.font.SysFont('Georgia', self.fontSize, bold=self.bold)
        label = font.render(self.txt, True, self.fontColor)
        self.width = label.get_width()
        screen.blit(label, (self.x, self.y))


class Timer:
    def __init__(self, duration, repeat=False, autostart=False, func=None) -> None:
        self.duration = duration
        self.startTime = 0
        self.active = False
        self.repeat = repeat
        self.func= func
        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.startTime = get_ticks()

    def deactivate(self):
        self.active = False
        self.startTime = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            currentTime = get_ticks()
            if currentTime - self.startTime >= self.duration:
                if self.func: self.func()
                self.deactivate()



#helper function to center sprites
def drawCenteringLines(screen):
    #vertical lines
    pygame.draw.rect(screen, 'black', pygame.Rect(240,0,5,1000))
    pygame.draw.rect(screen, 'black', pygame.Rect(600,0,5,1000))
    pygame.draw.rect(screen, 'black', pygame.Rect(960,0,5,1000))

    #horz lines
    pygame.draw.rect(screen, 'black', pygame.Rect(0,100,1200,5))
    pygame.draw.rect(screen, 'black', pygame.Rect(0,400,1200,5))
    pygame.draw.rect(screen, 'black', pygame.Rect(0,700,1200,5))
