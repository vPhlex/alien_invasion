import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def_init_(self):
    """Initialize the game, and create game resources."""
    pygame.init()

    self.screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")