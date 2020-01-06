# Import Pygame library
import pygame


# Globals
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

UP = 0
DOWN = 1

FPS = 75 # Change this to your display refresh rate for best result
isGameFinished = False
screenWidth = 1000
screenHeight = 600

playerX, playerY = 30, screenHeight/2
playerSpeed = 5
movePlayer = [False, False]

computerX, computerY = screenWidth-50, screenHeight/2
computerSpeed = 4

ballX, ballY = screenWidth/2, screenHeight/2
ballRadius = 8
ballSpeed = 7

padHeight, padWidth = 100, 20


# Initialize Pygame
pygame.init()


# Create display
screen = pygame.display.set_mode((screenWidth, screenHeight))


# Create clock
clock = pygame.time.Clock()


# Main loop
while not isGameFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameFinished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movePlayer[UP] = True
            if event.key == pygame.K_s:
                movePlayer[DOWN] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movePlayer[UP] = False
            if event.key == pygame.K_s:
                movePlayer[DOWN] = False

    # Player movement
    if movePlayer[UP]:
        playerY -= playerSpeed
    if movePlayer[DOWN]:
        playerY += playerSpeed

    # Player boundary collision
    if playerY < 10:
        playerY = 10
    if playerY > (screenHeight - padHeight - 10):
        playerY = (screenHeight - padHeight - 10)


    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, WHITE, pygame.Rect(playerX, playerY, padWidth, padHeight))

    # Draw computer
    pygame.draw.rect(screen, WHITE, pygame.Rect(computerX, computerY, padWidth, padHeight))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (int(ballX), int(ballY)), ballRadius)

    pygame.display.flip()
    clock.tick(FPS)


# Close Pygame
pygame.quit()