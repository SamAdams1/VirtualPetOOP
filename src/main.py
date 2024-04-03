import pygame, button, pet
import button
import pet

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
font = pygame.font.SysFont('Georgia', 40, bold=True)
clock.tick(60)  # limits FPS to 60

pygame.display.set_caption('Virtual Pet Simulator')


#helper function to center sprites
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
blueBirdNormal = pygame.image.load('images/pets/blue_bird_normal.png').convert_alpha()
blueBirdHappy = pygame.image.load('images/pets/blue_bird_happy.png').convert_alpha()
blueBirdSick = pygame.image.load('images/pets/blue_bird_yuck.png').convert_alpha()

yellowBirdNormal = pygame.image.load('images/pets/yellow_bird_normal.png').convert_alpha()
yellowBirdHappy = pygame.image.load('images/pets/yellow_bird_happy.png').convert_alpha()
yellowBirdSick = pygame.image.load('images/pets/yellow_bird_yuck.png').convert_alpha()

redBirdNormal = pygame.image.load('images/pets/red_bird_normal.png').convert_alpha()
redBirdHappy = pygame.image.load('images/pets/red_bird_happy.png').convert_alpha()
redBirdSick = pygame.image.load('images/pets/red_bird_yuck.png').convert_alpha()


bluebird = pet.Pet("Dan", "blue", 80,225, blueBirdNormal, blueBirdHappy)#240-160
yellowbird = pet.Pet("Ian", "yellow", 440,225, yellowBirdNormal, yellowBirdHappy)#600-160
redbird = pet.Pet("Jan", "red", 800,225, redBirdNormal, redBirdHappy)#960-160

#load button images
choosePetLabel = pygame.image.load('images/buttons/choosepet.png').convert_alpha()
choosePetHover = pygame.image.load('images/buttons/choosepethover.png').convert_alpha()
playButton = button.Button(425,650, choosePetLabel,choosePetHover)

petChoice = None

running = True
while running:
    screen.fill("gray")

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # render game here
    # playButton.fix(screen)
    if playButton.draw(screen) and petChoice != None:
        print(petChoice)
    elif bluebird.draw(screen):
        print('blue')
        petChoice = bluebird
    elif yellowbird.draw(screen):
        print('yellow')
        petChoice = yellowbird
    elif redbird.draw(screen):
        print('red')
        petChoice = redbird


    # drawCenteringLines()
    pygame.display.update()


pygame.quit()