import pygame.surface
import random
import directions as dirs
import colors as col
import globals as glob

class Player:
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.isMoving = [False, False] # When created the player should not move without any input first
    def checkCollision(self):
        if self.y <= 10:
            self.y = 10
        if self.y >= (glob.SCREEN_HEIGHT - self.height - 10):
            self.y = (glob.SCREEN_HEIGHT - self.height - 10)
    def setMovement(self, direction, move):
        self.isMoving[direction] = move
    def move(self):
        if self.isMoving[dirs.UP]:
            self.y -= self.speed
        if self.isMoving[dirs.DOWN]:
            self.y += self.speed
    def update(self):
        self.checkCollision()
        self.move()
    def draw(self, screen):
        pygame.draw.rect(screen, col.WHITE, pygame.Rect(self.x, self.y, self.width, self.height))

class Computer:
    def __init__ (self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
    def draw(self, screen):
        pygame.draw.rect(screen, col.WHITE, pygame.Rect(self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.directions = [False, False, False, False] # The ball has 8 directions, up, down, left, right and combinations of those that wouldn't cancel each other out
        self.direction = dirs.RIGHT # Always start towards the computer
    def setDirection(self, ):
        if self.direction == 0:  # Up
            self.directions[dirs.UP] = True
            self.directions[dirs.DOWN] = False
            self.directions[dirs.LEFT] = False
            self.directions[dirs.RIGHT] = False
        elif self.direction == 1:  # Down
            self.directions[dirs.DOWN] = True
            self.directions[dirs.UP] = False
            self.directions[dirs.LEFT] = False
            self.directions[dirs.RIGHT] = False
        elif self.direction == 2:  # Left
            self.directions[dirs.LEFT] = True
            self.directions[dirs.RIGHT] = False
            self.directions[dirs.UP] = False
            self.directions[dirs.DOWN] = False
        elif self.direction == 3:  # Right
            self.directions[dirs.RIGHT] = True
            self.directions[dirs.LEFT] = False
            self.directions[dirs.UP] = False
            self.directions[dirs.DOWN] = False
        elif self.direction == 4:  # Up + left
            self.directions[dirs.UP] = True
            self.directions[dirs.LEFT] = True
            self.directions[dirs.DOWN] = False
            self.directions[dirs.RIGHT] = False
        elif self.direction == 5:  # Up + right
            self.directions[dirs.UP] = True
            self.directions[dirs.RIGHT] = True
            self.directions[dirs.LEFT] = False
            self.directions[dirs.DOWN] = False
        elif self.direction == 6:  # Down + left
            self.directions[dirs.DOWN] = True
            self.directions[dirs.LEFT] = True
            self.directions[dirs.UP] = False
            self.directions[dirs.RIGHT] = False
        elif self.direction == 7:  # Down + right
            self.directions[dirs.DOWN] = True
            self.directions[dirs.RIGHT] = False
            self.directions[dirs.UP] = False
            self.directions[dirs.LEFT] = False
    def move(self):
        if self.directions[dirs.UP]:
            self.y -= self.speed
        if self.directions[dirs.DOWN]:
            self.y += self.speed
        if self.directions[dirs.LEFT]:
            self.x -= self.speed
        if self.directions[dirs.RIGHT]:
            self.x += self.speed
    def update(self):
        self.setDirection()
        self.move()
    def draw(self, screen):
        pygame.draw.circle(screen, col.WHITE, (int(self.x), int(self.y)), self.radius)