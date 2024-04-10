import pygame
import gui

class Pet(gui.Button):
    def __init__(self, name, color, x, y, img, hoverImg, barMax,sickImg=None, ):
        super().__init__(x, y, img, hoverImg)
        self.name = name
        self.color = color
        self.hat = None

        self.holdImg = img
        self.sickImg = sickImg
        self.barMax = barMax
        self.stats = {
            'health': barMax,
            'hunger': barMax,
            'clean': barMax,
            'energy': barMax,
            'mood': barMax,
        }
    def changeStat(self, statIndex, value):
        if self.stats[statIndex] <= self.barMax:
            self.stats[statIndex] += value
            #dont allow stats to go over or under 0/100
            if self.stats[statIndex] > self.barMax:
                self.stats[statIndex] = self.barMax
            elif self.stats[statIndex] < 0:
                self.stats[statIndex] = 0

