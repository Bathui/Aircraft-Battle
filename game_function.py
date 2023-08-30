import sys  # player could quit the game
import pygame


def check_events_settings(AB_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                AB_settings.gameInterface = False



def check_events(ship, AB_settings):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            # if event.key == pygame.K_SPACE:
            #     AB_settings.GameInterface = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False
def change_screen(AB_settings):
    if AB_settings.gameInterface == False:
        AB_settings.image = pygame.image.load('/Users/sai/pythonProjects/Aircraft-Battle/materials/Background.jpg')
        # /Users/sai/pythonProjects/Aircraft-Battle/materials/Start interface.png
        # D:\Aircraft\Aircraft-Battle\materials\Start interface.png
def update_screen(ship, screen, image):
    screen.blit(image, (0, 0))
    ship.blitme()
    pygame.display.flip()
