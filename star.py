import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a star. Used to decorate the background."""

    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # The following code was added to try to make the star images have a
        # background that blends in with the light gray background specified in
        # the Settings class.
        white = (255, 255, 255)
        self.image.set_colorkey(white)
        self.image.convert_alpha()
