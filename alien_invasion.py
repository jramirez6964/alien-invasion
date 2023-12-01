import sys  # Contains tools that allow us to exit the game when the player
            # quits.

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize the background settings.
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create a display window to draw the game's graphical elements.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # The attribute called screen is called a surface.
        pygame.display.set_caption("Alien Invasion")

        # Draw a ship right after the game window has been created.
        # Call to Ship() requires one argument.
        # self argument here refers to the current instance of AlienInvasion.
        self.ship = Ship(self)  

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:  # This infinite while loop is controlled by an event loop.
            # This loop contains code to manage events and manage screen updates.
            # An event is an action the user performs while playing the game.

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            # Make the clock tick.
            self.clock.tick(60)  # This is a frame rate of 60 times per second.

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()