# Import libraries
import pygame
import random


# Globals
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

FPS = 75 # Change this to your display refresh rate for best result
isGameFinished = False
screenWidth = 1000
screenHeight = 600

computerX, computerY = screenWidth-50, screenHeight/2
computerSpeed = 4

ballX, ballY = screenWidth/2, screenHeight/2
ballRadius = 8
ballSpeed = 7
ballDirection = [False, False, False, False] # The ball has 8 directions, UP, DOWN, LEFT, RIGHT and combinations such as UP+LEFT or DOWN+RIGHT
ballDirectionNumber = random.randint(0, 7) # Eight possible directions, 0 up to 7 makes 8 possible numbers

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


# Initialize Pygame
pygame.init()


# Create display
screen = pygame.display.set_mode((screenWidth, screenHeight))


# Create objects
player = Player(30, screenHeight/2, 100, 20, 5)

# Create clock
clock = pygame.time.Clock()


# Main loop
while not isGameFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameFinished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move[UP] = True
            if event.key == pygame.K_s:
                player.move[DOWN] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.move[UP] = False
            if event.key == pygame.K_s:
                player.move[DOWN] = False

    # Player movement
    if player.move[UP]:
        player.y -= player.speed
    if player.move[DOWN]:
        player.y += player.speed

    # Set ball direction based on the direction number
    if ballDirectionNumber == 0: #UP
        ballDirection[UP] = True
        ballDirection[DOWN] = False
        ballDirection[LEFT] = False
        ballDirection[RIGHT] = False
    elif ballDirectionNumber == 1: # DOWN
        ballDirection[DOWN] = True
        ballDirection[UP] = False
        ballDirection[LEFT] = False
        ballDirection[RIGHT] = False
    elif ballDirectionNumber == 2: # LEFT
        ballDirection[LEFT] = True
        ballDirection[RIGHT] = False
        ballDirection[UP] = False
        ballDirection[DOWN] = False
    elif ballDirectionNumber == 3: # RIGHT
        ballDirection[RIGHT] = True
        ballDirection[LEFT] = False
        ballDirection[UP] = False
        ballDirection[DOWN] = False
    elif ballDirectionNumber == 4: # UP + LEFT
        ballDirection[UP] = True
        ballDirection[LEFT] = True
        ballDirection[DOWN] = False
        ballDirection[RIGHT] = False
    elif ballDirectionNumber == 5: # UP + RIGHT
        ballDirection[UP] = True
        ballDirection[RIGHT] = True
        ballDirection[LEFT] = False
        ballDirection[DOWN] = False
    elif ballDirectionNumber == 6: # DOWN + LEFT
        ballDirection[DOWN] = True
        ballDirection[LEFT] = True
        ballDirection[UP] = False
        ballDirection[RIGHT] = False
    elif ballDirectionNumber == 7: # DOWN + RIGHT
        ballDirection[DOWN] = True
        ballDirection[RIGHT] = False
        ballDirection[UP] = False
        ballDirection[LEFT] = False

    # Ball movement
    if ballDirection[UP]:
        ballY -= ballSpeed
    if ballDirection[DOWN]:
        ballY += ballSpeed
    if ballDirection[LEFT]:
        ballX -= ballSpeed
    if ballDirection[RIGHT]:
        ballX += ballSpeed

    # Player boundary collision
    if player.y < 10:
        player.y = 10
    if player.y > (screenHeight - player.height - 10):
        player.y = (screenHeight - player.height - 10)


    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, WHITE, pygame.Rect(player.x, player.y, player.width, player.height))

    # Draw computer
    pygame.draw.rect(screen, WHITE, pygame.Rect(computerX, computerY, padWidth, padHeight))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (int(ballX), int(ballY)), ballRadius)

    pygame.display.flip()
    clock.tick(FPS)


# Close Pygame
pygame.quit()