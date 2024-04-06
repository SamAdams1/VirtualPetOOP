import pygame
import gui
import pet
import rooms

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
clock.tick(60)  # limits FPS to 60

pygame.display.set_caption('Virtual Pet Simulator')
logo = pygame.image.load('images/buttons/windowlogo.png').convert_alpha()
pygame.display.set_icon(logo)


running = True
while running:
    screen.fill("gray")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                rooms.userTxtInput = rooms.userTxtInput[:-1]
            else:
                rooms.userTxtInput += event.unicode

    # render game here
    rooms.displayRooms(screen)
    rooms.warningLabel.draw(screen)
    # gui.drawCenteringLines()


    pygame.display.update()


pygame.quit()