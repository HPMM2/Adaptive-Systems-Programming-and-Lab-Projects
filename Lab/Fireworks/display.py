import math
import random
import pygame
import sys

def explotar(posx, posy, radio):
	for i in range(radio):
		screen.fill((255,255,255))
		for speed, angle in particles:
			distance = i * speed
			x = posx + distance * math.cos(angle)
			y = posy + distance * math.sin(angle)
			screen.set_at((int(x), int(y)), (0,0,0))
		pygame.display.flip()


pygame.init()

x = 300
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]


explotar(400,400,399)
explotar(50,50,100)
explotar(550,600,200)
