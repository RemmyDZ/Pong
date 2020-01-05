# Importeer de Pygame library
import pygame


# Globale variabelen/constanten
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

UP = 0
DOWN = 1

FPS = 60
isGameFinished = False
screenWidth = 1000
screenHeight = 600

playerX, playerY = 30, screenHeight/2
playerSpeed = 5
movePlayer = [False, False]

computerX, computerY = screenWidth-50, screenHeight/2
computerSpeed = 4


# Pygame initialiseren
pygame.init()


# Display aanmaken
screen = pygame.display.set_mode((screenWidth, screenHeight))


#Klok aanmaken
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

    if movePlayer[UP]:
        playerY -= playerSpeed
    if movePlayer[DOWN]:
        playerY += playerSpeed


    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, pygame.Rect(playerX, playerY, 20, 100))
    pygame.draw.rect(screen, WHITE, pygame.Rect(computerX, computerY, 20, 100))
    pygame.display.flip()
    clock.tick(FPS)


# Pygame afsluiten
pygame.quit()