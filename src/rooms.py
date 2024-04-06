import pygame
import gui, pet
import doublyLinkedList as dll

#load pet images
blueBirdNormal = pygame.image.load('images/pets/blue_bird_normal.png')
blueBirdHappy = pygame.image.load('images/pets/blue_bird_happy.png')
blueBirdSick = pygame.image.load('images/pets/blue_bird_yuck.png')

yellowBirdNormal = pygame.image.load('images/pets/yellow_bird_normal.png')
yellowBirdHappy = pygame.image.load('images/pets/yellow_bird_happy.png')
yellowBirdSick = pygame.image.load('images/pets/yellow_bird_yuck.png')

redBirdNormal = pygame.image.load('images/pets/red_bird_normal.png')
redBirdHappy = pygame.image.load('images/pets/red_bird_happy.png')
redBirdSick = pygame.image.load('images/pets/red_bird_yuck.png')

bluebird = pet.Pet("Dan", "blue", 80,225, blueBirdNormal, blueBirdHappy)#240-160
yellowbird = pet.Pet("Ian", "yellow", 440,225, yellowBirdNormal, yellowBirdHappy)#600-160
redbird = pet.Pet("Jan", "red", 800,225, redBirdNormal, redBirdHappy)#960-160
petChoice = bluebird


#start menu
startMenuTitle = pygame.image.load('images/buttons/title.png')
startLabel = pygame.image.load('images/buttons/start.png')
startHover = pygame.image.load('images/buttons/startHover.png')
startButton = gui.Button(475,650, startLabel,startHover)

#choose pet
enterLabel = pygame.image.load('images/buttons/enter.png')
enterHover = pygame.image.load('images/buttons/enterHover.png')
enterButton = gui.Button(475,650, enterLabel,enterHover)
enterNameTitle = pygame.image.load('images/entername.png')
choosePetTitle = pygame.image.load('images/choosepet.png')


#home
homeImg = pygame.image.load('images/home.jpg')
homeImg = pygame.transform.scale(homeImg, (1200,800))
homeLabel = pygame.image.load('images/buttons/home.png')
homeHover = pygame.image.load('images/buttons/homeHover.png')
homeButton = gui.Button(950,0, homeLabel,homeHover)


#vet
vetImg = pygame.image.load('images/vet.jpg')
vetImg = pygame.transform.scale(vetImg, (1200,800))
vetLabel = pygame.image.load('images/buttons/vet.png')
vetHover = pygame.image.load('images/buttons/vetHover.png')
vetButton = gui.Button(740,0, vetLabel,vetHover)



#HUD
healthbar = gui.HealthBar(0,55, 300,40,100, 'green')
healthLabel = gui.Label(f"Health: {petChoice.hungerLvl*20}%",'black',20,True, healthbar.x, healthbar.y)

hungerbar = gui.HealthBar(0,100, 300,40,100, 'royalblue')
hungerLabel = gui.Label(f"Hunger: {petChoice.hungerLvl*20}%",'black',20,True, hungerbar.x, hungerbar.y)

cleanbar = gui.HealthBar(0,145, 300,40,100, 'orange')
cleanLabel = gui.Label(f"Cleanliness: {petChoice.cleanLvl*20}%",'black',20,True, cleanbar.x, cleanbar.y)

energybar = gui.HealthBar(0,190, 300,40,100, 'yellow')
energyLabel = gui.Label(f"Energy: {petChoice.cleanLvl*20}%",'black',20,True, energybar.x, energybar.y)

moodLabel = gui.Label(f"Mood: {petChoice.mood}",'black',20,True, 0, 235)

# nxt room
rightArrowImg = pygame.image.load('images/buttons/rightarrow.png')
leftArrowImg = pygame.image.load('images/buttons/leftarrow.png')
rightButton = gui.Button(1100,400, rightArrowImg,rightArrowImg)
leftButton = gui.Button(0,400, leftArrowImg,leftArrowImg)



warningTxt = "example warning example warning example warning example warning"
warningLabel = gui.Label('','red',40,True, 10,750)
warningLabel.txt = warningTxt

#determine which screen to show
startMenu = True
choosePetScreen = False
enterNameScreen = False
homeScreen = False
vetScreen = False

pygame.init()
font = pygame.font.SysFont('Georgia', 40, bold=True)
txtBox = pygame.Rect(483,590, 250,50) 
def drawTxtBox(screen):
    pygame.draw.rect(screen, 'black', txtBox, 5)
    textInput = font.render(userTxtInput, True, 'black')
    screen.blit(textInput,(txtBox.x + 5, txtBox.y + 5))

    txtBox.w = max(250,textInput.get_width() + 10)

# def warningLabel():
#     warning = font.render(warningTxt, True, 'red')
#     screen.blit(warning,(10,750))


def drawPet(screen):
        petChoice.button.topleft = (440,225)
        petChoice.draw(screen)

def nxtRoomBtns(screen):
    rightButton.draw(screen)
    leftButton.draw(screen)
    roomlst = list(roomDict.keys())
    roomIndex = 0
    # if 
    for index, i in enumerate(roomDict.keys()):
        print(i, index)
        if i == currentRoom:
            roomIndex = index
            print(roomIndex)

nameBg = pygame.Rect(0,0, 265,50)
def petHUD(screen):
    pygame.draw.rect(screen, 'white', nameBg)
    petName = gui.Label(petChoice.name, 'black',40,True,0,0)
    petName.draw(screen)
    nameBg.w = max(0,petName.width + 5)

    healthbar.draw(screen)
    healthLabel.draw(screen)
    hungerbar.draw(screen)
    hungerLabel.draw(screen)
    cleanbar.draw(screen)
    cleanLabel.draw(screen)
    energybar.draw(screen)
    energyLabel.draw(screen)
    moodLabel.draw(screen)

    # nxtRoomBtns(screen)

def displayRooms(screen):
    if startMenu:
        displayStartMenu(screen)
    if choosePetScreen:
        displayChoosePet(screen)
    if enterNameScreen:
        displayEnterNameScreen(screen)
    if vetScreen:
        displayVet(screen)
    if homeScreen:
        displayBedroom(screen)
    if not (startMenu or choosePetScreen):
        drawPet(screen)

def displayStartMenu(screen):
    screen.blit(startMenuTitle, (0,100))
    if startButton.draw(screen):
        global startMenu, choosePetScreen
        startMenu = False
        choosePetScreen = True

def displayChoosePet(screen):
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
def displayEnterNameScreen(screen):
    screen.blit(enterNameTitle,(0,50))
    drawTxtBox(screen)
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

def displayBedroom(screen):
    screen.blit(homeImg, (0,0))
    petHUD(screen)
    if vetButton.draw(screen):
        global homeScreen, vetScreen
        homeScreen = False
        vetScreen = True

def displayBathroom(screen):
    pass
def displayKitchen(screen):
    pass
def displayPlayroom(screen):
    pass

def displayVet(screen):
    screen.blit(vetImg, (0,0))
    petHUD(screen)
    if homeButton.draw(screen):
        global homeScreen, vetScreen
        homeScreen = True
        vetScreen = False


# currentRoom = 'Bedroom'
# roomDict = {
#     'start': displayStartMenu(),
#     'choosePet': displayChoosePet(),
#     'enterName': displayEnterNameScreen(),
#     'Bedroom': displayBedroom(),
#     'Bathroom': displayBathroom(),
#     'Kitchen': displayKitchen(),
#     'Playroom': displayPlayroom(),
#     'Vet': displayVet(),
# }