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

#create 3 pet objects 
bluebird = pet.Pet("Dan", "blue", 80,225, blueBirdNormal, blueBirdHappy, 100, blueBirdSick)#240-160
yellowbird = pet.Pet("Ian", "yellow", 440,225, yellowBirdNormal, yellowBirdHappy, 100, yellowBirdSick)#600-160
redbird = pet.Pet("Jan", "red", 800,225, redBirdNormal, redBirdHappy, 100, redBirdSick)#960-160
petChoice = bluebird


BTN_X = 475
BTN_Y = 635
#start menu
startMenuTitle = pygame.image.load('images/titles/title.png')
startLabel = pygame.image.load('images/buttons/start.png')
startHover = pygame.image.load('images/buttons/startHover.png')
startButton = gui.Button(BTN_X,BTN_Y, startLabel,startHover)

#choose pet
enterLabel = pygame.image.load('images/buttons/enter.png')
enterHover = pygame.image.load('images/buttons/enterHover.png')
enterButton = gui.Button(BTN_X,BTN_Y, enterLabel,enterHover)
enterNameTitle = pygame.image.load('images/titles/entername.png')
choosePetTitle = pygame.image.load('images/titles/choosepet.png')

#home
homeImg = pygame.image.load('images/backgrounds/home.jpg')
homeImg = pygame.transform.scale(homeImg, (1200,800))
sleepNormal = pygame.image.load('images/buttons/sleep.png')
sleepHover = pygame.image.load('images/buttons/sleephover.png')
sleepButton = gui.Button(BTN_X,BTN_Y, sleepNormal,sleepHover)


#vet
vetImg = pygame.image.load('images/backgrounds/vet2.jpg')
vetImg = pygame.transform.scale(vetImg, (1200,800))
treatNormal = pygame.image.load('images/buttons/treat.png')
treatHover = pygame.image.load('images/buttons/treathover.png')
treatButton = gui.Button(BTN_X,BTN_Y, treatNormal,treatHover)

#bathroom
bathroomImg = pygame.image.load('images/backgrounds/bathroom.jpg')
bathroomImg = pygame.transform.scale(bathroomImg, (1200,800))
washNormal = pygame.image.load('images/buttons/wash.png')
washHover = pygame.image.load('images/buttons/washhover.png')
washButton = gui.Button(BTN_X,BTN_Y, washNormal, washHover)

#kitchen
kitchenImg = pygame.image.load('images/backgrounds/kitchen.jpg')
kitchenImg = pygame.transform.scale(kitchenImg, (1200,800))
feedNormal = pygame.image.load('images/buttons/feed.png')
feedHover = pygame.image.load('images/buttons/feedhover.png')
feedButton = gui.Button(BTN_X,BTN_Y, feedNormal,feedHover)

#playroom
playroomImg = pygame.image.load('images/backgrounds/playroom.jpg')
playroomImg = pygame.transform.scale(playroomImg, (1200,800))
playNormal = pygame.image.load('images/buttons/play.png')
playHover = pygame.image.load('images/buttons/playhover.png')
playButton = gui.Button(BTN_X,BTN_Y, playNormal,playHover)


#HUD
healthbar = gui.HealthBar(0,55, 300,40,100, 'green')
healthLabel = gui.Label(f"Health: {petChoice.healthLvl}%",'black',20,True, healthbar.x, healthbar.y)

hungerbar = gui.HealthBar(0,100, 300,40,100, 'royalblue')
hungerLabel = gui.Label(f"Hunger: {petChoice.hungerLvl}%",'black',20,True, hungerbar.x, hungerbar.y)

cleanbar = gui.HealthBar(0,145, 300,40,100, 'orange')
cleanLabel = gui.Label(f"Cleanliness: {petChoice.cleanLvl}%",'black',20,True, cleanbar.x, cleanbar.y)

energybar = gui.HealthBar(0,190, 300,40,100, 'yellow')
energyLabel = gui.Label(f"Energy: {petChoice.energyLvl}%",'black',20,True, energybar.x, energybar.y)

moodBar = gui.HealthBar(0,235, 300,40,100, 'purple')
moodLabel = gui.Label(f"Mood: Happy",'black',20,True, 0, 235)

# next room buttons
rightArrowImg = pygame.image.load('images/buttons/right.png')
rightHoverImg = pygame.image.load('images/buttons/righthover.png')
rightButton = gui.Button(800,0, rightArrowImg,rightHoverImg)

leftArrowImg = pygame.image.load('images/buttons/left.png')
leftHoverImg = pygame.image.load('images/buttons/lefthover.png')
leftButton = gui.Button(500,0, leftArrowImg,leftHoverImg)
blankImg = pygame.image.load('images/buttons/blank.png')
blankImg = pygame.transform.scale(blankImg, (800,99))

#gives user feedback
warningLabel = gui.Label('','red',40,True, 10,750)
warningLabel.txt = "example warning example warning example warning example warning"

#display what user named pet or default name
nameLabelBg = pygame.Rect(0,0, 265,50)
petNameLabel = gui.Label(petChoice.name, 'black',40,True,0,0)

#shows the current and next rooms
currentRoom = 'Bedroom'
leftRoomLabel = gui.Label('Vet','black',30,True,490,25)
currentRoomLabel = gui.Label(currentRoom,'black',30,True,640,25)
rightRoomLabel = gui.Label('Bathroom','black',30,True,950,25)

# elements to draw on the screen
hudElements = [
    leftRoomLabel,currentRoomLabel,rightRoomLabel,
    petNameLabel,
    healthbar, healthLabel,
    hungerbar, hungerLabel, 
    cleanbar, cleanLabel, 
    energybar, energyLabel,
    moodBar, moodLabel,
]

pygame.init()
font = pygame.font.SysFont('Georgia', 40, bold=True)
txtBox = pygame.Rect(483,590, 250,50)


def drawTxtBox(screen):
    pygame.draw.rect(screen, 'black', txtBox, 5)
    textInput = font.render(userTxtInput, True, 'black')
    screen.blit(textInput,(txtBox.x + 5, txtBox.y + 5))

    txtBox.w = max(250,textInput.get_width() + 10)

intialStart = True
def drawPet(screen):
    global intialStart
    if intialStart:
        intialStart = False
        petChoice.healthLvl -= 47
        petChoice.hungerLvl -= 73
        petChoice.cleanLvl -= 86
        petChoice.energyLvl -= 58
        petChoice.moodLvl = 25

    updateTimers()
    petChoice.button.topleft = (440,225)
    petChoice.draw(screen)
    petChoice.img = petChoice.holdImg



def nxtRoomBtns(screen):
    leftRoomLabel.txt = roomsDLL.pointer.prev.data
    leftRoomLabel.x = 490 - leftRoomLabel.width
    rightRoomLabel.txt = roomsDLL.pointer.next.data

    if leftButton.draw(screen):
        roomsDLL.pointer = roomsDLL.pointer.prev
    if rightButton.draw(screen):
        roomsDLL.pointer = roomsDLL.pointer.next
    
    currentRoomLabel.txt = roomsDLL.pointer.data



def petHUD(screen):
    pygame.draw.rect(screen, 'white', nameLabelBg)
    petNameLabel.txt = petChoice.name
    nameLabelBg.w = max(0,petNameLabel.width + 5)
    screen.blit(blankImg, (330,0))
    
    for element in hudElements:
        element.draw(screen)
    
    updateBarsnLbls()
    nxtRoomBtns(screen)


def displayRooms(screen):
    roomDict[currentRoomLabel.txt](screen)
    if currentRoomLabel.txt != 'start' and currentRoomLabel.txt != 'choosePet':
        drawPet(screen)
        if currentRoomLabel.txt != 'enterName':
            petHUD(screen)



def displayStartMenu(screen):
    screen.blit(startMenuTitle, (0,100))
    if startButton.draw(screen):
        global petChoice
        petChoice = None
        currentRoomLabel.txt = 'choosePet'
   

def displayChoosePet(screen):
    screen.blit(choosePetTitle,(150,50))
    global petChoice
    if enterButton.draw(screen) and petChoice != None:
        currentRoomLabel.txt = 'enterName'
        warningLabel.txt = ''
    if bluebird.draw(screen):
        petChoice = bluebird
        warningLabel.txt = 'Choose the blue bird?'
    if yellowbird.draw(screen):
        petChoice = yellowbird
        warningLabel.txt = 'Choose the yellow bird?'
    if redbird.draw(screen):
        petChoice = redbird
        warningLabel.txt = 'Choose the red bird?'



charLimit = 12
userTxtInput = ""
showBtn = True
def displayEnterNameScreen(screen):
    global showBtn
    if showBtn:
        screen.blit(enterNameTitle,(0,50))
        drawTxtBox(screen)
    if enterButton.draw(screen):
        if len(userTxtInput) <= charLimit:
            petChoice.name = str(userTxtInput)
            warningLabel.txt = ""
            
            showBtn = False
            pygame.time.delay(100) #delay room change so sleep btn is not pressed
            currentRoomLabel.txt = 'Bedroom'
        else:
            warningLabel.txt = f"Pet name cannot be over {charLimit} characters long."



class PetNeeds():
    def __init__(self) -> None:
        self.dimScreen = False

        self.addEnergyVal = 1
        self.addCleanVal = 3
        self.reduceHungerVal = 10
        self.addHealthVal = 10
        self.addMoodVal = 25
petNeeds = PetNeeds()

# Create a transparent surface
transparent_surface = pygame.Surface((1200, 800), pygame.SRCALPHA)
transparent_surface.fill((10, 0, 0, 200))
dimScreen = False
sleepTimeWait = False

def displayBedroom(screen):
    screen.blit(homeImg, (0,0))
    if petNeeds.dimScreen:
        screen.blit(transparent_surface, (0,0))
        petChoice.img = petChoice.hoverImg


    else:
        petChoice.img = petChoice.holdImg

    if sleepButton.draw(screen):
        petNeeds.dimScreen = not petNeeds.dimScreen
        if petNeeds.dimScreen:
            timers['sleep'].activate()
        else:
            timers['sleep'].deactivate()




def displayBathroom(screen):
    screen.blit(bathroomImg, (0,0))
    if washButton.draw(screen):
        petChoice.wash(petNeeds.addCleanVal)



def displayKitchen(screen):
    screen.blit(kitchenImg, (0,0))
    if feedButton.draw(screen):
        petChoice.feed(petNeeds.reduceHungerVal)


def displayPlayroom(screen):
    screen.blit(playroomImg, (0,0))
    if playButton.draw(screen):
        petChoice.play(petNeeds.addMoodVal)


def displayVet(screen):
    screen.blit(vetImg, (0,0))
    if treatButton.draw(screen):
        petChoice.treat(petNeeds.addHealthVal)

def updateBarsnLbls():
    healthbar.hp = petChoice.healthLvl
    hungerbar.hp = petChoice.hungerLvl
    cleanbar.hp = petChoice.cleanLvl
    energybar.hp = petChoice.energyLvl
    moodBar.hp = petChoice.moodLvl

    healthLabel.txt = f"Health: {petChoice.healthLvl}%"
    hungerLabel.txt = f"Hunger: {petChoice.hungerLvl}%"
    cleanLabel.txt = f"Cleanliness: {petChoice.cleanLvl}%"
    energyLabel.txt = f"Energy: {petChoice.energyLvl}%"

    if moodBar.hp < petChoice.barMax // 2:
        petChoice.mood = "Sad"
    else:
        petChoice.mood = "Happy"

    moodLabel.txt = f"Mood: {petChoice.mood}"


def updateEnergy():
    petChoice.sleep(petNeeds.addEnergyVal*-1)

def updateTimers():
    for i in timers.keys():
        timers[i].update()

timers = {
    'sleep': gui.Timer(1000, func=updateEnergy, repeat=True),
    'health': gui.Timer(10000, func=updateEnergy, repeat=True, autostart=True),
    'hunger': gui.Timer(10000, func=updateEnergy, repeat=True, autostart=True),
    'clean': gui.Timer(10000, func=updateEnergy, repeat=True, autostart=True),
    'energy': gui.Timer(10000, func=updateEnergy, repeat=True, autostart=True),
    'mood': gui.Timer(10000, func=updateEnergy, repeat=True, autostart=True),
}

roomDict = {
    'start': displayStartMenu,
    'choosePet': displayChoosePet,
    'enterName': displayEnterNameScreen,
    'Bedroom': displayBedroom,
    'Bathroom': displayBathroom,
    'Kitchen': displayKitchen,
    'Playroom': displayPlayroom,
    'Vet': displayVet
}
roomsDLL = dll.createCDLL(list(roomDict.keys())[3:])
roomsDLL.pointer = roomsDLL.search(currentRoom)

# roomsDLL.printList()