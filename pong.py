# PONG pygame from https://gist.github.com/vinothpandian/4337527

import _random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

#colors from RGB Color Codes Chart
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT /2
ball_pos = [0,0]
bal_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)  #skąd liczby po przecinku? w docs pygame ich nie ma
pygame.dislay.set_caption("Hello World")                  #zmiana nazwy okna

#helper function that spawns a ball, returns a position vector and a velocity vector
#if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)

    if right == False:
        horz = - horz

    ball_vel = [horz, -vert]

#define event handlers
