import pygame


class Ship:
    def __init__(self, screen, Bf_settings):
        """Initialize the ship and starting position"""
        self.screen = screen
        # obtain the object from Settings
        self.Bf_settings = Bf_settings
        # Load the ship image, and the parameter is the address of the image
        self.image = pygame.image.load('D:\Aircraft\Aircraft-Battle\materials\Spitfire\Movement0000.png')
        # /Users/sai/pythonProjects/Aircraft-Battle/materials/P51 Mustang/Reverse0000.png
        # D:\Aircraft\Aircraft-Battle\materials\Spitfire\Movement0000.png
        # This function is to get ship's rectangle
        # We can treat the ship image like a rectangle, even if it is not shaped like rectangle
        # rect can make us use x-and y-coordinate
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # store the value of x-coordinate of the ship
        # match the screen's centerx
        self.rect.centerx = self.screen_rect.centerx

        self.center = float(self.rect.centerx)
        # store the value of y-coordinate of the ship's bottom
        # match the screen's value of the bottom
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # Draw the ship at the location we set
        # blitme() method will draw the ship at the position self.rect

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.Bf_settings.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.Bf_settings.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
# and self.rect.top < self.screen_rect.top
# and self.rect.bottom < self.screen_rect.bottom