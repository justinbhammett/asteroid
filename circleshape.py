import pygame
from constants import PLAYER_RADIUS

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, PLAYER_RADIUS):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = PLAYER_RADIUS

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass