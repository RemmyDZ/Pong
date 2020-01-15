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

class Ball:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = [False, False, False, False] # The ball has 8 directions, up, down, left, right and combinations of those that wouldn't cancel each other out
        self.directionNumber = random.randint(0, 7)
    def setDirection(self):
        if self.directionNumber == 0:  # Up
            self.direction[dirs.UP] = True
            self.direction[dirs.DOWN] = False
            self.direction[dirs.LEFT] = False
            self.direction[dirs.RIGHT] = False
        elif self.directionNumber == 1:  # Down
            self.direction[dirs.DOWN] = True
            self.direction[dirs.UP] = False
            self.direction[dirs.LEFT] = False
            self.direction[dirs.RIGHT] = False
        elif self.directionNumber == 2:  # Left
            self.direction[dirs.LEFT] = True
            self.direction[dirs.RIGHT] = False
            self.direction[dirs.UP] = False
            self.direction[dirs.DOWN] = False
        elif self.directionNumber == 3:  # Right
            self.direction[dirs.RIGHT] = True
            self.direction[dirs.LEFT] = False
            self.direction[dirs.UP] = False
            self.direction[dirs.DOWN] = False
        elif self.directionNumber == 4:  # Up + left
            self.direction[dirs.UP] = True
            self.direction[dirs.LEFT] = True
            self.direction[dirs.DOWN] = False
            self.direction[dirs.RIGHT] = False
        elif self.directionNumber == 5:  # Up + right
            self.direction[dirs.UP] = True
            self.direction[dirs.RIGHT] = True
            self.direction[dirs.LEFT] = False
            self.direction[dirs.DOWN] = False
        elif self.directionNumber == 6:  # Down + left
            self.direction[dirs.DOWN] = True
            self.direction[dirs.LEFT] = True
            self.direction[dirs.UP] = False
            self.direction[dirs.RIGHT] = False
        elif self.directionNumber == 7:  # Down + right
            self.direction[dirs.DOWN] = True
            self.direction[dirs.RIGHT] = False
            self.direction[dirs.UP] = False
            self.direction[dirs.LEFT] = False
    def move(self):
        if self.direction[dirs.UP]:
            self.y -= self.speed
        if self.direction[dirs.DOWN]:
            self.y += self.speed
        if self.direction[dirs.LEFT]:
            self.x -= self.speed
        if self.direction[dirs.RIGHT]:
            self.x += self.speed
    def update(self):
        self.setDirection()
        self.move()
    def draw(self, screen):
        pygame.draw.circle(screen, col.WHITE, (int(self.x), int(self.y)), self.radius)