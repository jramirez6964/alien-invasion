import sys  # Contains tools that allow us to exit the game when the player
            # quits.

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize the background settings.
        self.clock = pygame.time.Clock()

        # Create a display window to draw the game's graphical elements.
        self.screen = pygame.display.set_mode((1200, 800))  # 1200 wide by 800 long
        # The attribute called screen is called a surface.
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:  # This infinite while loop is controlled by an event loop.
            # This loop contains code to manage events and manage screen updates.
            # An event is an action the user performs while playing the game.

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # Make the clock tick.
            self.clock.tick(60)  # This is a frame rate of 60 times per second.

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()