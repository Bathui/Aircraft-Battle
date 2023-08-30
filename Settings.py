import pygame


class Settings():
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.gameInterface = True
        self.screen_width = 1425
        self.screen_height = 800

        self.image = pygame.image.load('/Users/sai/pythonProjects/Aircraft-Battle/materials/Start interface.png')
        # 'D:\Aircraft\Aircraft-Battle\materials\Background.jpg'
        #

        # for event in pygame.event.get():
        #     if event.type == pygame.K_SPACE:
        #         self.image = pygame.image.load('D:\Aircraft\Aircraft-Battle\materials\Background.jpg')
        #
        #     else:
        #         self.image = pygame.image.load('D:\Aircraft\Aircraft-Battle\materials\Start interface.png')



