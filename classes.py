class Player:
    def __init__(self, x, y, height, width, speed):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.move = [False, False] # When created the player should not move without any input first

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