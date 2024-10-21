import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rndAngle = random.uniform(20, 50)
        ang1 = self.velocity.rotate(rndAngle)
        ang2 = self.velocity.rotate(-rndAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newAss1 = Asteroid(self.position.x, self.position.y, newRadius)
        newAss2 = Asteroid(self.position.x, self.position.y, newRadius)
        newAss1.velocity = ang1 * 1.2
        newAss2.velocity = ang2 * 1.2
