from circleshape import *
from constants import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        CircleShape.__init__(self,x,y,radius)
        self.radius = SHOT_RADIUS
        self.velocity = velocity
    
    def draw(self, screen):
        WHITE = (255,255,255)
        pygame.draw.circle(screen, WHITE, (self.position.x ,self.position.y) ,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    