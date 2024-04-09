import pygame
import gui

class Pet(gui.Button):
    def __init__(self, name, color, x, y, img, hoverImg, barMax,sickImg=None, ):
        super().__init__(x, y, img, hoverImg)
        self.name = name
        self.color = color
        self.hat = None

        self.holdImg = img
        
        self.barMax = barMax
        self.healthLvl = barMax 
        self.hungerLvl = barMax
        self.cleanLvl = barMax
        self.energyLvl = barMax
        self.moodLvl = barMax
        self.mood = "Happy"

    def feed(self, foodValue):
        if self.hungerLvl < self.barMax:
            self.hungerLvl += foodValue
            if self.hungerLvl > self.barMax:
                self.hungerLvl = self.barMax
    
    def sleep(self, sleepValue):
        if self.energyLvl < self.barMax:
            self.energyLvl += sleepValue
            if self.energyLvl > self.barMax:
                self.energyLvl = self.barMax

    def treat(self, treatmentVal):
        if self.healthLvl < self.barMax:
            self.healthLvl += treatmentVal
            if self.healthLvl > self.barMax:
                self.healthLvl = self.barMax

    def play(self, playVal):
        if self.moodLvl < self.barMax:
            self.moodLvl += playVal
            if self.moodLvl > self.barMax:
                self.moodLvl = self.barMax

    def wash(self, washVal):
        if self.cleanLvl < self.barMax:
            self.cleanLvl += washVal
            if self.cleanLvl > self.barMax:
                self.cleanLvl = self.barMax
