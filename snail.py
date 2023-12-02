import pygame

class Snail:
    """
    Part of the exercise on p. 138 to make a new game character appear on the 
    screen.
    """

    def __init__(self, ai_game):
        """Initialize a snail at the center of the game surface."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/snail.bmp')

        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the snail at its current location."""
        self.screen.blit(self.image, self.rect)