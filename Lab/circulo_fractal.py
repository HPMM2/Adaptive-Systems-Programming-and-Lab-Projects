import tkinter as tk
import sys

def fractal(inicio2, fin2, delta):
    inicio2= inicio2+delta
    fin2= fin2 - delta
    if (fin2>inicio2):
        c.create_oval(inicio2,inicio2,fin2,fin2, fill="#ffffff",outline="#000000")
        fractal(inicio2, fin2, delta)

if(len(sys.argv)<3):
    print("Necesito tres argumentos: 1.- Inicio, 2.- Fin, 3.- Delta")
    sys.exit(1)
else:
    inicio=int(sys.argv[1])
    fin=int(sys.argv[2])
    delta=int(sys.argv[3]) #delta es el espacio que vamos a dejar entre un anillo y otro
    
    if(delta<1):
        delta=5
	
    root=tk.Tk()
    c=tk.Canvas(root,width=600,height=600)
	
    c.create_oval(inicio,inicio,fin,fin, fill="#ffffff",outline="#000000")

    fractal(inicio, fin, delta)
    
    c.pack()
    c.mainloop()


