import pygame
import gui, pet
import json
import doublyLinkedList as dll
import random


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
birds = {
    'blue': pet.Pet("Dan", "blue", 80,225, blueBirdNormal, blueBirdHappy, 100, blueBirdSick),
    'yellow': pet.Pet("Ian", "yellow", 440,225, yellowBirdNormal, yellowBirdHappy, 100, yellowBirdSick),
    'red': pet.Pet("Jan", "red", 800,225, redBirdNormal, redBirdHappy, 100, redBirdSick),

}
petChoice = birds['blue']

saveData = {
    'name': '',
    'pet': None,
    'room': 'start',
    'health': petChoice.stats['health'],
    'hunger': petChoice.stats['hunger'],
    'clean': petChoice.stats['clean'],
    'energy': petChoice.stats['energy'],
    'mood': petChoice.stats['mood'],
}
def loadSave():
    petChoice.name = saveData['name']
    petChoice.stats['health'] = saveData['health']
    petChoice.stats['hunger'] = saveData['hunger']
    petChoice.stats['clean'] = saveData['clean']
    petChoice.stats['energy'] = saveData['energy']
    petChoice.stats['mood'] = saveData['mood']
try: 
    # the file already exists 
    with open('save.txt') as load_file: 
        saveData = json.load(load_file) 
except: 
    # create the file and store initial values 
    with open('save.txt', 'w') as store_file: 
        json.dump(saveData, store_file)

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

#items
thermometer = pygame.image.load('images/items/thermometer.png')
thermometer = pygame.transform.scale(thermometer, (200,200))

#HUD
healthbar = gui.HealthBar(0,55, 300,40,100, 'green')
healthLabel = gui.Label(f"Health: {petChoice.stats['health']}%",'black',20,True, healthbar.x, healthbar.y)

hungerbar = gui.HealthBar(0,100, 300,40,100, 'royalblue')
hungerLabel = gui.Label(f"Hunger: {petChoice.stats['hunger']}%",'black',20,True, hungerbar.x, hungerbar.y)

cleanbar = gui.HealthBar(0,145, 300,40,100, 'orange')
cleanLabel = gui.Label(f"Cleanliness: {petChoice.stats['clean']}%",'black',20,True, cleanbar.x, cleanbar.y)

energybar = gui.HealthBar(0,190, 300,40,100, 'yellow')
energyLabel = gui.Label(f"Energy: {petChoice.stats['energy']}%",'black',20,True, energybar.x, energybar.y)

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
warningLabel.txt = ""

#display what user named pet or default name
nameLabelBg = pygame.Rect(0,0, 265,50)
petNameLabel = gui.Label(petChoice.name, 'black',40,True,0,0)

#shows the current and next rooms
currentRoom = saveData['room']
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
    firstStart()

    petAccessories(screen)
    updateTimers()
    petChoice.button.topleft = (440,225)
    petChoice.draw(screen)
    petChoice.img = petChoice.holdImg

def petAccessories(screen):
    if healthbar.hp < petChoice.barMax // 2:
        screen.blit(thermometer, (320, 370))
    # if hungerbar.hp < petChoice.barMax // 2:
    #     screen.blit(thermometer, (320, 370))
    # if cleanbar.hp < petChoice.barMax // 2:
    #     screen.blit(thermometer, (320, 370))
    # if energybar.hp < petChoice.barMax // 2:
    #     screen.blit(thermometer, (320, 370))

def firstStart():
    global intialStart
    if intialStart:
        intialStart = False
        loadSave()
        for key in petChoice.stats.keys():
            petChoice.changeStat(key, -1*random.randrange(10,50))

def nxtRoomBtns(screen):
    if not roomsDLL.pointer:
        roomsDLL.pointer = roomsDLL.search(currentRoomLabel.txt)

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

    if enterButton.draw(screen) and saveData['pet'] != None:
        currentRoomLabel.txt = 'enterName'
        warningLabel.txt = ''
    if birds['blue'].draw(screen):
        choosePet('blue')

    if birds['yellow'].draw(screen):
        choosePet('yellow')
        
    if birds['red'].draw(screen):
        choosePet('red')


def choosePet(color):
    global petChoice
    petChoice = birds[color]
    saveData['pet'] = color
    warningLabel.txt = f"Choose the {color} bird?"


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
            pygame.time.delay(200) #delay room change so sleep btn is not pressed
            currentRoomLabel.txt = 'Bedroom'
        else:
            warningLabel.txt = f"Pet name cannot be over {charLimit} characters long."


# Create a transparent surface
transparent_surface = pygame.Surface((1200, 800), pygame.SRCALPHA)
transparent_surface.fill((10, 0, 0, 200))
dimScreen = False
sleepTimeWait = False

def displayBedroom(screen):
    screen.blit(homeImg, (0,0))
    if interactWPet['dim']:
        screen.blit(transparent_surface, (0,0))
        petChoice.img = petChoice.hoverImg

    else:
        petChoice.img = petChoice.holdImg

    if sleepButton.draw(screen):
        interactWPet['dim'] = not interactWPet['dim']
    if interactWPet['dim'] and not timers['sleep'].active:
        timers['sleep'].activate()
    elif not interactWPet['dim'] and timers['sleep'].active:
        timers['sleep'].deactivate()


def displayBathroom(screen):
    timers['sleep'].deactivate()
    screen.blit(bathroomImg, (0,0))
    if washButton.draw(screen):
        petChoice.changeStat('clean', interactWPet['addClean'])


def displayKitchen(screen):
    screen.blit(kitchenImg, (0,0))
    if feedButton.draw(screen):
        petChoice.changeStat('hunger',interactWPet['reduceHunger'])


def displayPlayroom(screen):
    screen.blit(playroomImg, (0,0))
    if playButton.draw(screen):
        petChoice.changeStat('mood',interactWPet['addMood'])


def displayVet(screen):
    timers['sleep'].deactivate()
    screen.blit(vetImg, (0,0))
    if treatButton.draw(screen):
        petChoice.changeStat('health',interactWPet['addHealth'])


def updateBarsnLbls():
    healthbar.hp = petChoice.stats['health']
    hungerbar.hp = petChoice.stats['hunger']
    cleanbar.hp = petChoice.stats['clean']
    energybar.hp = petChoice.stats['energy']
    moodBar.hp = petChoice.stats['mood']

    healthLabel.txt = f"Health: {petChoice.stats['health']}%"
    hungerLabel.txt = f"Hunger: {petChoice.stats['hunger']}%"
    cleanLabel.txt = f"Cleanliness: {petChoice.stats['clean']}%"
    energyLabel.txt = f"Energy: {petChoice.stats['energy']}%"

    if moodBar.hp < petChoice.barMax // 2:
        moodLabel.txt = "Mood: Sad"
    else:
        moodLabel.txt = "Mood: Happy"

    


# petChoice.stats['health']
def updateEnergy():
    petChoice.changeStat('energy',interactWPet['addEnergy'])

def updateTimers():
    for key in timers.keys():
        timers[key].update()

def lowerStats(statKey, reduceKey):
    petChoice.changeStat(statKey, reduceStats[reduceKey])

def updateSaveData():
    saveData['name'] = petChoice.name
    saveData['room'] = currentRoomLabel.txt
    saveData['health'] = petChoice.stats['health']
    saveData['hunger'] = petChoice.stats['hunger']
    saveData['clean'] = petChoice.stats['clean']
    saveData['energy'] = petChoice.stats['energy']
    saveData['mood'] = petChoice.stats['mood']



interactWPet = {
    'dim': False,
    'addEnergy': 3,
    'addClean': 7,
    'reduceHunger': 9,
    'addHealth': 13,
    'addMood': 11,
}

reduceStats = {
    'reduceEnergy': -1,
    'reduceClean': -1,
    'addHunger': -1,
    'reduceHealth': -3,
    'reduceMood': -2,
}

timers = {
    #increases stat
    'sleep': gui.Timer(1000, func=updateEnergy, repeat=True),

    #lowers stat
    'energy': gui.Timer(10000, func=lambda: lowerStats('energy', 'reduceEnergy'), repeat=True, autostart=True),
    'health': gui.Timer(20000, func=lambda: lowerStats('health', 'reduceHealth'), repeat=True, autostart=True),
    'hunger': gui.Timer(9500, func=lambda: lowerStats('hunger', 'addHunger'), repeat=True, autostart=True),
    'clean': gui.Timer(9000, func=lambda: lowerStats('clean', 'reduceClean'), repeat=True, autostart=True),
    'mood': gui.Timer(15000, func=lambda: lowerStats('mood', 'reduceMood'), repeat=True, autostart=True),
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