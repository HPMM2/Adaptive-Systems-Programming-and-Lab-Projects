import tkinter as tk
import sys
import random

root = tk.Tk()
c = tk.Canvas(root, width=280, height=280)

colors = {
    "a": "#ffff00", "c": "#00ffff", "d": "#ffc90e", "m": "#800080", "r": "#ff0000", "v": "#00bb00"
}

archivo = sys.argv[1]
f = open(archivo, 'r')

configuracion_floodit14=f.readlines()
y0=0
y1=20

for i in range(14):
    x0 = 0
    x1 = 20
    patroncolor = configuracion_floodit14[i].strip()
    for j in range(14):
        c.create_rectangle(x0, y0, x1, y1, fill=colors[patroncolor[j]], outline="")
        x0 = x0+20
        x1 = x1+20
    y0 = y0+20
    y1 = y1+20

f.close()
c.pack()
c.mainloop()




#Ejemplo de una configuración de color para una línea del tablero
#configuracion="caccrrrvmdracm"
#c.create_rectangle(0,0,20,20,fill="#ff0000",outline="black")
#Codigo ejemplo para crear un rectangulo