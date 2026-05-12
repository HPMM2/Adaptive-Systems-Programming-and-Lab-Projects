import math
import random
import pygame

def explotar(posx, posy, radio):
	for i in range(radio):
		screen.fill((255,255,255))
		for speed, angle in particles:
			distance = i * speed
			x = posx + distance * math.cos(angle)
			y = posy + distance * math.sin(angle)
			screen.set_at((int(x), int(y)), (0,0,0))
		pygame.display.flip()

def secuencia_explosiones(posx, posy, radio, secuencia):
    for i in range(secuencia):
        explotar(posx, posy, radio)


pygame.init()
screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]



for i in range(5):
    secuencia_explosiones(400,400,399,1)
    secuencia_explosiones(50,50,100,1)
    secuencia_explosiones(550,600,200,1)


#Analisis - Los Ositos
#El codigo que se analizo no tenia la llamada explotar() mas sus parametros por lo cual no podia ejecutarse el programa con el pygame.init()
#Una vez agregado pasamos a crear la secuencia para que la funcion explotar() pudiera repetirse, agregamos la variable secuencia en secuencia_explosiones()
#mas las variables ya establecidas en explotar() para que conociera sus valores y despues dentro de la nueva variable secuencia_explosiones() 
#llamamos a la funcion explotar(), para que se pudiera repetir usamos solamente el for y range para el ciclo.

#cambiamos la llamada explotar() (que usamos para que corriera el programa que habiamos usado desde un inicio) a la llamada de la secuencia 
#secuencia_explosiones() y agregamos los parametros.
#Para que fuera un poco mas automatico agregamos un ciclo for con range de 5 para que la secuencia siguiera 5 veces en total. 