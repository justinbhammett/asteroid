import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	clock = pygame.time.Clock()
	dt = 0
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shootable = pygame.sprite.Group()
	AsteroidField.containers = (updateable,)
	Asteroid.containers = (asteroids, updateable, drawable)
	Player.containers = (updateable, drawable)
	Shot.containers = (updateable, drawable, shootable)

	shots = []
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
	asteroid_field = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		dt = clock.tick(60) / 1000

		for upd in updateable:
			upd.update(dt)
		for object in asteroids:
			if (object.is_colliding_with(player)):
				print("Game over!")
				raise SystemExit()
			for shot in shots:
				if (object.is_colliding_with(shot)):
					object.split()
					shot.kill()
		for drw in drawable:
			drw.draw(screen)
		pygame.display.flip()


if __name__ == "__main__":
	main()

