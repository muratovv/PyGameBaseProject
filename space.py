__author__ = 'Федор'
import random
import pygame
import math


class Space:

    def __init__(self, resolution, quantity, speed):
        self.speed = speed
        self.stars = []
        self.resolution = resolution
        self.quantity = quantity
        self.center = [self.resolution[0]//2, self.resolution[1]//2]
        for i in range(quantity):
            x = random.randrange(0, self.resolution[0])
            y = random.randrange(0, self.resolution[1])
            z = random.randrange(1, 3)
            self.stars.append([x, y, z])
        self.eps = 3


    def show(self, display):
        for star in self.stars:
            pygame.draw.circle(display, (255, 255, 255), list(map(int, star[:2])), star[2])
        # pygame.draw.circle(display, (125, 125, 125), self.center[0:2], 3)

    def fly(self, display):
        for i in range(len(self.stars)):
            offsetX = self.speed * (self.stars[i][0] - self.center[0]) / self.resolution[0]
            offsetY = self.speed * (self.stars[i][1] - self.center[1]) / self.resolution[1]
            self.stars[i][0] += offsetX
            self.stars[i][1] += offsetY
            if offsetX == offsetY == 0:
                print(i, self.stars[i][0], self.stars[i][1])
        self.update()
        self.show(display)

    def action(self, display):
        self.fly(display)

    def changeSpeed(self, speed):
        if speed >= 0:
            self.speed = speed
    def update(self):
        for i in range(len(self.stars)):
            if self.stars[i][0] < 0 or self.stars[i][0] > self.resolution[0] or \
            self.stars[i][1] < 0 or self.stars[i][1] > self.resolution[1]:
                x = random.randrange(0, self.resolution[0])
                y = random.randrange(0, self.resolution[1])
                z = random.randrange(1, 3)
                self.stars[i] = [x, y, z]
