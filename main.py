import pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
font = pygame.font.SysFont('Georgia', 40, bold=True)
clock.tick(60)  # limits FPS to 60

pygame.display.set_caption('Virtual Pet Simulator')


class Button:
    def __init__(self, x, y, img, hoverImg) -> None:
        self.img = img
        self.hoverImg = hoverImg
        self.currentImg = None
        self.button = self.img.get_rect()
        self.button.topleft = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, (110, 110, 110), self.button)
        screen.blit(self.img, (self.button.x + 5, self.button.y + 5))

    def hover(self):
        pos = pygame.mouse.get_pos()
        if self.button.collidepoint(pos):
            self.currentImg = self.hoverImg
        else:
            self.currentImg = self.img
        screen.blit(self.currentImg, (self.button.x, self.button.y))

    def render(self):
        # Turns the pet class into a pygame surface
        # Create a surface with the specified width and height
        pet_surface = pygame.Surface((self.img.get_width(),self.img.get_height())).convert_alpha()
        # Fill the surface with the color of the pet
        pet_surface.fill((0,0,0,0))
        # Assuming image is a pygame.Surface representing the appearance of the pet
        # You can blit the image onto the surface, adjust the position as needed
        pet_surface.blit(self.img, (0, 0))  # Assuming the image starts at position (0, 0) on the surface
        return pet_surface  



class Pet(Button):
    def __init__(self, name, color, x, y, img, hoverImg, sickImg=None) -> None:
        super().__init__(x, y, img, hoverImg)
        self.name = name
        self.color = color
        self.hat = None

        self.hungerLvl = 5 #0-5
        self.cleanLvl = 5 #0-5
        self.mood = 'happy' #happy - sad - hungry
    
    def feed(self, foodValue):
        self.hunger += foodValue

def drawCenteringLines():
    #vertical lines
    pygame.draw.rect(screen, 'black', pygame.Rect(240,0,5,1000)) 
    pygame.draw.rect(screen, 'black', pygame.Rect(600,0,5,1000))
    pygame.draw.rect(screen, 'black', pygame.Rect(960,0,5,1000))

    #horz lines
    pygame.draw.rect(screen, 'black', pygame.Rect(0,100,1200,5))
    pygame.draw.rect(screen, 'black', pygame.Rect(0,400,1200,5))
    pygame.draw.rect(screen, 'black', pygame.Rect(0,700,1200,5))



#load pet images
blueBirdNormal = pygame.image.load('images/blue_bird_normal.png').convert_alpha()
blueBirdHappy = pygame.image.load('images/blue_bird_happy.png').convert_alpha()
blueBirdSick = pygame.image.load('images/blue_bird_yuck.png').convert_alpha()

yellowBirdNormal = pygame.image.load('images/yellow_bird_normal.png').convert_alpha()
yellowBirdHappy = pygame.image.load('images/yellow_bird_happy.png').convert_alpha()
yellowBirdSick = pygame.image.load('images/yellow_bird_yuck.png').convert_alpha()

redBirdNormal = pygame.image.load('images/red_bird_normal.png').convert_alpha()
redBirdHappy = pygame.image.load('images/red_bird_happy.png').convert_alpha()
redBirdSick = pygame.image.load('images/red_bird_yuck.png').convert_alpha()


bluebird = Pet("Dan", "blue", 80,225, blueBirdNormal, blueBirdHappy)#240-160
yellowbird = Pet("Ian", "yellow", 440,225, yellowBirdNormal, yellowBirdHappy)#600-160
redbird = Pet("Jan", "red", 800,225, redBirdNormal, redBirdHappy)#960-160

#load button images
choosePetLabel = pygame.image.load('buttonImages/choosepet.png').convert_alpha()
choosePetHover = pygame.image.load('buttonImages/choosepethover.png').convert_alpha()
playButton = Button(425,650, choosePetLabel,choosePetHover)

petChoice = None

running = True
while running:
    screen.fill("gray")

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if playButton.button.collidepoint(event.pos) and petChoice != None:
                print(petChoice)
            elif bluebird.button.collidepoint(event.pos):
                print(event)
                petChoice = "blue"
            elif yellowbird.button.collidepoint(event.pos):
                print(event)   
                petChoice = "yellow"
            elif redbird.button.collidepoint(event.pos):
                print(event)
                petChoice = "red"


    # render game here
    # playButton.draw(screen)
    playButton.hover()
    
    bluebird.hover()
    yellowbird.hover()
    redbird.hover()

    # drawCenteringLines()



    pygame.display.update()
    


pygame.quit()