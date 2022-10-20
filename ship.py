import pygame

Class Ship:
    """"A class to manage the ship."""

    def_init_(self, ai_game):
    """Initialize the ship and set its starting position."""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    #Load the ship image and get its rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()