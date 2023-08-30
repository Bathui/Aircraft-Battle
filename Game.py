# exit game for users
import sys
import pygame
from ship import Ship
from Settings import Settings
import game_function as gf


def run_game():
    # Initialize background settings
    pygame.init()
    # to create a display window that is 1425 pixels wide
    # and  800 pixels high
    AB_settings = Settings()
    screen = pygame.display.set_mode((AB_settings.screen_width, AB_settings.screen_height))
    pygame.display.set_caption("Air Craft Battle Game")


    # Make a ship
    ship = Ship(screen)

    # this variable sets the background color
    # this tuple stores the rgb number of the background color
    # bg_color = (135, 206, 235)
    # image = pygame.image.load('D:\Aircraft\Aircraft-Battle\Background.jpg')
    # '/Users/sai/Desktop/dl/universe copy.jpg'

    #screen.blit(image, (0, 0))
    # watch for keyboard and mouse event

    while AB_settings.gameInterface:
        gf.check_events_settings(AB_settings)
        screen.blit(AB_settings.image, (0, 0))
        pygame.display.flip()

    gf.change_screen(AB_settings)


    while True:

        # the event is what users did
        gf.check_events(ship, AB_settings)

        # this function fill the color to the screen
        # parameter is given by the variable bg_color
        # screen.fill(bg_color)

        # ship.blitme()

        # pygame.display.filp() is to make the most drawn screen visible
        # with the while loop, the new screen can only be visible
        # pygame.display.flip()
        ship.update()
        gf.update_screen(ship, screen, AB_settings.image)






run_game()
