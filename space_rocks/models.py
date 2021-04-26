from pygame.math import Vector2
from utils import load_sprite

UP = Vector2(0, -1)

class GameObject:
	def __init__(self, position, sprite, velocity):
		self.position = Vector2(position)
		self.velocity = Vector2(velocity)
		self.radius = sprite.get_width() / 2
		self.sprite = sprite

	def draw(self, surface):
		blit_position = self.position - Vector2(self.radius)
		surface.blit(self.sprite, blit_position)

	def move(self):
		self.position = self.position + self.velocity

	def collides_with(self, other_obj):
		distance = self.position.distance_to(other_obj)
		return distance < self.radius + other_obj.radius

class SpaceShip(GameObject):
	# Angle in degrees that obj direction can rotate in each frame
	MANEUVERABILITY = 3
	def __init__(self, position):
		# Make a copy of the original UP vector
		self.direction = Vector2(UP)
		super().__init__(position, load_sprite("spaceship"), Vector2(0))

	def rotate(self, clockwise=True):
		sign = 1 if clockwise else -1
		amgle = self.MANEUVERABILITY * sign
		self.direction.rotate_ip(angle)