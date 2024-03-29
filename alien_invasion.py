import sys  # Contains tools that allow us to exit the game when the player
            # quits.

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize the background settings.
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create a display window to draw the game's graphical elements.
        # The attribute called screen is called a surface.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Draw a ship right after the game window has been created.
        # Call to Ship() requires one argument.
        # self argument here refers to the current instance of AlienInvasion.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_star_grid()
        self._create_fleet()

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:  # This infinite while loop is controlled by an event loop.
            # This loop contains code to manage events and manage screen updates.
            # An event is an action the user performs while playing the game.

            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)  # This is a frame rate of 60 times per second.

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_star_grid(self):
        """Create the grid of stars."""
        # Make a star and keep adding stars until there's no room left.
        # Spacing between stars shall be two star widths and two star heights.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width * 2, star_height * 2
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x + randint(-50, 50), 
                                  current_y + randint(-50, 50))
                current_x += 3 * star_width

            # Finished a row; reset x value, and increment y value
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid."""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)
    


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.stars.draw(self.screen)
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
