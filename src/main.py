import pygame
import json
import rooms


pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

pygame.display.set_caption('Virtual Pet Simulator')
logo = pygame.image.load('images/titles/windowlogo.png')
pygame.display.set_icon(logo)


running = True
while running:
    screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(rooms.petChoice)
            rooms.updateSaveData()
            print('quiting')
            with open('save.txt', 'w') as store_data:
                json.dump(rooms.saveData, store_data)
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                rooms.userTxtInput = rooms.userTxtInput[:-1]
            else:
                rooms.userTxtInput += event.unicode

    
    rooms.displayRooms(screen)
    rooms.warningLabel.draw(screen)
    # gui.drawCenteringLines()

    clock.tick(60)# limits FPS to 60
    pygame.display.update()
pygame.quit()