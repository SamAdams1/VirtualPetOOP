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
logo = pygame.image.load('images/buttons/windowlogo.png').convert_alpha()
pygame.display.set_icon(logo)


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

#start menu
startMenuTitle = pygame.image.load('images/buttons/title.png')
startLabel = pygame.image.load('images/buttons/start.png')
startHover = pygame.image.load('images/buttons/startHover.png')
startButton = button.Button(475,650, startLabel,startHover)

#choose pet
enterLabel = pygame.image.load('images/buttons/enter.png')
enterHover = pygame.image.load('images/buttons/enterHover.png')
enterButton = button.Button(475,650, enterLabel,enterHover)
enterNameTitle = pygame.image.load('images/entername.png')
choosePetTitle = pygame.image.load('images/choosepet.png')


#home
homeImg = pygame.image.load('images/home.jpg')
# homeImg = pygame.transform.scale_by(homeImg, 3.2)
homeImg = pygame.transform.scale(homeImg, (1200,800))



#vet
vetImg = pygame.image.load('images/vet.jpg')


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


def displayStartMenu():
    screen.blit(startMenuTitle, (0,100))
    if startButton.draw(screen):
        global startMenu, choosePetScreen
        startMenu = False
        choosePetScreen = True

def displayChoosePet():
    screen.blit(choosePetTitle,(150,50))
    global petChoice, choosePetScreen, enterNameScreen, warningTxt
    if enterButton.draw(screen) and petChoice != None:
        choosePetScreen = False
        enterNameScreen = True
        warningTxt = ''
    elif bluebird.draw(screen):
        petChoice = bluebird
        warningTxt = 'Choose the blue bird?'
    elif yellowbird.draw(screen):
        petChoice = yellowbird
        warningTxt = 'Choose the yellow bird?'
    elif redbird.draw(screen):
        petChoice = redbird
        warningTxt = 'Choose the red bird?'


charLimit = 10
userTxtInput = ""
warningTxt = "example warning example warning example warning example warning"
def displayEnterNameScreen():
    screen.blit(enterNameTitle,(0,50))
    drawTxtBox()
    if enterButton.draw(screen):
        if len(userTxtInput) <= charLimit:
            petChoice.name = userTxtInput
            global warningTxt
            warningTxt = ""
            
            global enterNameScreen, homeScreen
            enterNameScreen = False
            homeScreen = True
        else:
            warningTxt = f"Pet name cannot be over {charLimit} characters long."
    
txtBox = pygame.Rect(483,590, 250,50) 
def drawTxtBox():
    pygame.draw.rect(screen, 'black', txtBox, 5)
    textInput = font.render(userTxtInput, True, 'black')
    screen.blit(textInput,(txtBox.x + 5, txtBox.y + 5))

    txtBox.w = max(250,textInput.get_width() + 10)

def warningLabel():
    warning = font.render(warningTxt, True, 'red')
    screen.blit(warning,(10,750))
    

def displayHome():
    screen.blit(homeImg, (0,0))
    petHUD()

def displayVet():
    screen.blit(vetImg, (0,0))

nameBg = pygame.Rect(0,0, 265,50)
def petHUD():
    pygame.draw.rect(screen, 'white', nameBg)
    petName = font.render(petChoice.name, True, 'black')
    screen.blit(petName,(0,0))

    # nameBg.w = max(0,petName.get_width() + 5)



#determine which screen to show
startMenu = False
choosePetScreen = False
enterNameScreen = False
homeScreen = True
vetScreen = False



petChoice = bluebird
running = True
while running:
    screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                userTxtInput = userTxtInput[:-1]
            else:
                userTxtInput += event.unicode

    # render game here
    if startMenu:
        displayStartMenu()
    elif choosePetScreen:
        displayChoosePet()
    elif enterNameScreen:
        displayEnterNameScreen()
    elif homeScreen:
        displayHome()
    elif vetScreen:
        displayVet()
    if not (startMenu or choosePetScreen):
        petChoice.button.topleft = (440,225)
        petChoice.draw(screen)



    warningLabel()
    drawCenteringLines()


    pygame.display.update()


pygame.quit()