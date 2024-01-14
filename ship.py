import pygame

class Ship:
    """A class to manage the ship."""

    # The __init__ method has a parameter that is a reference to the current
    # instance of the AlienInvasion class because we want the Ship class to
    # access game resources defined in AlienInvasion.
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen  # Assign the screen to an attribute of 
        # Ship.
        self.settings = ai_game.settings
        # Get the screen's rect attribute and assign it to the Ship.
        self.screen_rect = ai_game.screen.get_rect() # Makes it easy to place 
        # the ship.

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship-rotated.bmp')
        # Access the picture's rect to assign it to the Ship.
        self.rect = self.image.get_rect()

        # Start each new ship at the middle left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
