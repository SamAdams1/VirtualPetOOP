import pygame
import gui

class Pet(gui.Button):
    def __init__(self, name, color, x, y, img, hoverImg, sickImg=None) -> None:
        super().__init__(x, y, img, hoverImg)
        self.name = name
        self.color = color
        self.hat = None

        self.hungerLvl = 5 #0-5
        self.cleanLvl = 5 #0-5
        self.mood = 'happy' #happy - sad
    
    def feed(self, foodValue):
        self.hunger += foodValue