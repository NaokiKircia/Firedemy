# PONG pygame from https://gist.github.com/vinothpandian/4337527

import _random
import pygame
import sys
from pygame import *
from easygui import *

pygame.init()
fps = pygame.time.Clock()

#colors from RGB Color Codes Chart
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#globals

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
ball_pos = [0, 0]
bal_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

#canvas declaration
# skad liczby po przecinku? w docs pygame ich nie ma
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
# zmiana nazwy okna
pygame.display.set_caption("Hello World")

#helper function that spawns a ball, returns a position vector and a velocity vector
#if right is True, spawn to the right, else spawn to the left
def ball_init (right):
    # these are vectors stored as lists
    global ball_pos, ball_vel
    ball_pos = [WIDTH//2, HEIGHT//2]
    horz = random.randrange(2, 4)
    vert = random.randrange(1, 3)

    if right == False:
        horz = - horz

    ball_vel = [horz, -vert]

#define event handlers
def init():
    #these are floats
    global paddle1_pos, paddle2_pos, paddle1_ve1, paddle2_ve2,l_score, r_score
    #these are int
    global score1, score2
    paddle1_pos = [HALF_PAD_WIDTH - 1, HEIGHT // 2]
    l_score = 0
    r_score = 0
    if random.randrage(0, 2) == 0:
        ball_init(True)
    else:
        ball_init(False)

#draw function of canvas
def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_poss, ball_vel, l_score, r_score

    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0], [WIDTH//2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH // 2, HEIGHT // 2], 70, 1)

    #update paddle's vertical position, kep paddle on the screen
