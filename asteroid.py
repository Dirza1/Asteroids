from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self,x,y,radius)
        self.radius = radius

    def draw(self, screen):
        WHITE = (255,255,255)
        pygame.draw.circle(screen, WHITE, (self.position.x ,self.position.y) ,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity1 * 1.2
        asteroid_2.velocity = new_velocity2 * 1.2
        group.add(asteroid_1)
        group.add(asteroid_2)