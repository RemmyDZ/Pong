# Import global libraries
import pygame
import random


# Import local libraries
import globals as glob
import colors as col
import directions as dirs # "dir" is already something in Python


# Globals
isGameFinished = False

ballX, ballY = glob.SCREEN_WIDTH/2, glob.SCREEN_HEIGHT/2
ballRadius = 8
ballSpeed = 7
ballDirection = [False, False, False, False]
ballDirectionNumber = random.randint(0, 7) # Eight possible directions, 0 dir.UP to 7 makes 8 possible numbers


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

class Ball:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = [False, False, False, False] # The ball has 8 directions, up, down, left, right and combinations of those that wouldn't cancel each other out

# Initialize Pygame
pygame.init()


# Create display
screen = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))


# Create objects
player = Player(30, glob.SCREEN_HEIGHT/2, glob.PAD_HEIGHT, glob.PAD_WIDTH, 5)
computer = Computer(glob.SCREEN_WIDTH-50, glob.SCREEN_HEIGHT/2, glob.PAD_HEIGHT, glob.PAD_WIDTH, 4)
ball = Ball(glob.SCREEN_WIDTH/2, glob.SCREEN_HEIGHT/2, 8, 7)

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
        ball.direction[dirs.UP] = True
        ball.direction[dirs.DOWN] = False
        ball.direction[dirs.LEFT] = False
        ball.direction[dirs.RIGHT] = False
    elif ballDirectionNumber == 1: # Down
        ball.direction[dirs.DOWN] = True
        ball.direction[dirs.UP] = False
        ball.direction[dirs.LEFT] = False
        ball.direction[dirs.RIGHT] = False
    elif ballDirectionNumber == 2: # Left
        ball.direction[dirs.LEFT] = True
        ball.direction[dirs.RIGHT] = False
        ball.direction[dirs.UP] = False
        ball.direction[dirs.DOWN] = False
    elif ballDirectionNumber == 3: # Right
        ball.direction[dirs.RIGHT] = True
        ball.direction[dirs.LEFT] = False
        ball.direction[dirs.UP] = False
        ball.direction[dirs.DOWN] = False
    elif ballDirectionNumber == 4: # Up + left
        ball.direction[dirs.UP] = True
        ball.direction[dirs.LEFT] = True
        ball.direction[dirs.DOWN] = False
        ball.direction[dirs.RIGHT] = False
    elif ballDirectionNumber == 5: # Up + right
        ball.direction[dirs.UP] = True
        ball.direction[dirs.RIGHT] = True
        ball.direction[dirs.LEFT] = False
        ball.direction[dirs.DOWN] = False
    elif ballDirectionNumber == 6: # Down + left
        ball.direction[dirs.DOWN] = True
        ball.direction[dirs.LEFT] = True
        ball.direction[dirs.UP] = False
        ball.direction[dirs.RIGHT] = False
    elif ballDirectionNumber == 7: # Down + right
        ball.direction[dirs.DOWN] = True
        ball.direction[dirs.RIGHT] = False
        ball.direction[dirs.UP] = False
        ball.direction[dirs.LEFT] = False

    # Ball movement
    if ball.direction[dirs.UP]:
        ball.y -= ball.speed
    if ball.direction[dirs.DOWN]:
        ball.y += ball.speed
    if ball.direction[dirs.LEFT]:
        ball.x -= ball.speed
    if ball.direction[dirs.RIGHT]:
        ball.x += ball.speed

    # Player boundary collision
    if player.y < 10:
        player.y = 10
    if player.y > (glob.SCREEN_HEIGHT - player.height - 10):
        player.y = (glob.SCREEN_HEIGHT - player.height - 10)


    screen.fill(col.BLACK)

    # Draw player
    pygame.draw.rect(screen, col.WHITE, pygame.Rect(player.x, player.y, player.width, player.height))

    # Draw computer
    pygame.draw.rect(screen, col.WHITE, pygame.Rect(computer.x, computer.y, computer.width, computer.height))

    # Draw ball
    pygame.draw.circle(screen, col.WHITE, (int(ball.x), int(ball.y)), ball.radius)

    pygame.display.flip()
    clock.tick(glob.FPS)


# Close Pygame
pygame.quit()