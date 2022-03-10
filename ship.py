import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        """Initialize the ship & set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        from game import resource_path
        ship_img_url = resource_path('images/ship.bmp')
        self.image = pygame.image.load(ship_img_url)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self) -> None:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)

    def center_ship(self) -> None:
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
