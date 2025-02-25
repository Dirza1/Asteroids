from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self,x,y,radius)
        self.radius = radius

    def draw(self, screen):
        WHITE = (255,255,255)
        pygame.draw.circle(screen, WHITE, (self.position.x ,self.position.y) ,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt