# Import global libraries
import pygame
import random

# Import local libraries
import globals as glob
import colors as col
import directions as dirs # "dir" is already something in Python
import classes

ballDirectionNumber = random.randint(0, 7) # Eight possible directions, 0 dir.UP to 7 makes 8 possible numbers

# Initialize Pygame
pygame.init()

# Create display
screen = pygame.display.set_mode((glob.SCREEN_WIDTH, glob.SCREEN_HEIGHT))

# Create objects
player = classes.Player(30, glob.SCREEN_HEIGHT/2, glob.PAD_HEIGHT, glob.PAD_WIDTH, 5)
computer = classes.Computer(glob.SCREEN_WIDTH-50, glob.SCREEN_HEIGHT/2, glob.PAD_HEIGHT, glob.PAD_WIDTH, 4)
ball = classes.Ball(glob.SCREEN_WIDTH/2, glob.SCREEN_HEIGHT/2, 8, 7)

# Create clock
clock = pygame.time.Clock()

# Main function
def main(isGameFinished):
    while not isGameFinished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameFinished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isGameFinished = True
                if event.key == pygame.K_w:
                    player.setMovement(dirs.UP, True)
                if event.key == pygame.K_s:
                    player.setMovement(dirs.DOWN, True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.setMovement(dirs.UP, False)
                if event.key == pygame.K_s:
                    player.setMovement(dirs.DOWN, False)

        # Update objects
        ball.update()
        player.update()

        screen.fill(col.BLACK)

        # Draw objects
        player.draw(screen)
        computer.draw(screen)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(glob.FPS)

    # Close Pygame
    pygame.quit()

# Run main function
if __name__ == '__main__':
    main(False)