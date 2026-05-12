import math
import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]

#Explosion

def explotar(posx, posy, radio, particulas):
    for i in range(radio):
        screen.fill((255,255,255))
        for speed, angle in particulas:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (0,0,0))



     pygame.display.flip()

        explotar(400,400,100,particles)
        explotar(50,50,100, particles)
        explotar(550,600,200, particles)

