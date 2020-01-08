# Import global libraries
import pygame
import random


# Import local libraries
import colors as col
import directions as dirs # "dir" is already something in Python


# Globals
FPS = 75 # Change this to your display refresh rate for best result
isGameFinished = False
screenWidth = 1000
screenHeight = 600

ballX, ballY = screenWidth/2, screenHeight/2
ballRadius = 8
ballSpeed = 7
ballDirection = [False, False, False, False] # The ball has 8 directions, up, down, left, right and combinations of those that wouldn't cancel each other out
ballDirectionNumber = random.randint(0, 7) # Eight possible directions, 0 dir.UP to 7 makes 8 possible numbers

padHeight, padWidth = 100, 20


# Classes
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


# Initialize Pygame
pygame.init()


# Create display
screen = pygame.display.set_mode((screenWidth, screenHeight))


# Create objects
player = Player(30, screenHeight/2, 100, 20, 5)
computer = Computer(screenWidth-50, screenHeight/2, 100, 20, 4)

# Create clock
clock = pygame.time.Clock()


# Main loop
while not isGameFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameFinished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move[dirs.UP] = True
            if event.key == pygame.K_s:
                player.move[dirs.DOWN] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.move[dirs.UP] = False
            if event.key == pygame.K_s:
                player.move[dirs.DOWN] = False

    # Player movement
    if player.move[dirs.UP]:
        player.y -= player.speed
    if player.move[dirs.DOWN]:
        player.y += player.speed

    # Set ball direction based on the direction number
    if ballDirectionNumber == 0: # Up
        ballDirection[dirs.UP] = True
        ballDirection[dirs.DOWN] = False
        ballDirection[dirs.LEFT] = False
        ballDirection[dirs.RIGHT] = False
    elif ballDirectionNumber == 1: # Down
        ballDirection[dirs.DOWN] = True
        ballDirection[dirs.UP] = False
        ballDirection[dirs.LEFT] = False
        ballDirection[dirs.RIGHT] = False
    elif ballDirectionNumber == 2: # Left
        ballDirection[dirs.LEFT] = True
        ballDirection[dirs.RIGHT] = False
        ballDirection[dirs.UP] = False
        ballDirection[dirs.DOWN] = False
    elif ballDirectionNumber == 3: # Right
        ballDirection[dirs.RIGHT] = True
        ballDirection[dirs.LEFT] = False
        ballDirection[dirs.UP] = False
        ballDirection[dirs.DOWN] = False
    elif ballDirectionNumber == 4: # Up + left
        ballDirection[dirs.UP] = True
        ballDirection[dirs.LEFT] = True
        ballDirection[dirs.DOWN] = False
        ballDirection[dirs.RIGHT] = False
    elif ballDirectionNumber == 5: # Up + right
        ballDirection[dirs.UP] = True
        ballDirection[dirs.RIGHT] = True
        ballDirection[dirs.LEFT] = False
        ballDirection[dirs.DOWN] = False
    elif ballDirectionNumber == 6: # Down + left
        ballDirection[dirs.DOWN] = True
        ballDirection[dirs.LEFT] = True
        ballDirection[dirs.UP] = False
        ballDirection[dirs.RIGHT] = False
    elif ballDirectionNumber == 7: # Down + right
        ballDirection[dirs.DOWN] = True
        ballDirection[dirs.RIGHT] = False
        ballDirection[dirs.UP] = False
        ballDirection[dirs.LEFT] = False

    # Ball movement
    if ballDirection[dirs.UP]:
        ballY -= ballSpeed
    if ballDirection[dirs.DOWN]:
        ballY += ballSpeed
    if ballDirection[dirs.LEFT]:
        ballX -= ballSpeed
    if ballDirection[dirs.RIGHT]:
        ballX += ballSpeed

    # Player boundary collision
    if player.y < 10:
        player.y = 10
    if player.y > (screenHeight - player.height - 10):
        player.y = (screenHeight - player.height - 10)


    screen.fill(col.BLACK)

    # Draw player
    pygame.draw.rect(screen, col.WHITE, pygame.Rect(player.x, player.y, player.width, player.height))

    # Draw computer
    pygame.draw.rect(screen, col.WHITE, pygame.Rect(computer.x, computer.y, computer.width, computer.height))

    # Draw ball
    pygame.draw.circle(screen, col.WHITE, (int(ballX), int(ballY)), ballRadius)

    pygame.display.flip()
    clock.tick(FPS)


# Close Pygame
pygame.quit()