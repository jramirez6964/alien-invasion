import pygame

class Ship:
    """A class to manage the ship."""

    # The __init__ method has a parameter that is a reference to the current
    # instance of the AlienInvasion class because we want the Ship class to
    # access game resources defined in AlienInvasion.
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen  # Assign the screen to an attribute of Ship.
        # Get the screen's rect attribute and assign it to the Ship.
        self.screen_rect = ai_game.screen.get_rect() # Makes it easy to place the ship.

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.image.set_colorkey((230, 230, 230))
        # Access the picture's rect to assign it to the Ship.
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)