from typing import Union
import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien & set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image & get it's `rect` attribute.
        from game import resource_path
        alien_img_url = resource_path('images/alien.bmp')
        self.image = pygame.image.load(alien_img_url)
        self.rect = self.image.get_rect()

        # Start each new alien near the top center of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)

        self.rect.x = self.x

    def check_edges(self) -> Union[bool, None]:
        """Return True if alien is at right edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.left >= screen_rect.right or self.rect.left <= 0:
            return True