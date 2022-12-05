import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

class Particle:
  def __init__(self, s_vel, gravity, window_size, pos):
    self.x = pos[0]
    self.y = pos[1]
    self.xvel = s_vel[0]
    self.yvel = s_vel[1]
    self.Gravity = gravity
    self.window_x = window_size[0]
    self.window_y = window_size[1]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()