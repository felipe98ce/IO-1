import math
import random
import Tkinter as tk
from Tkinter import *
xx=[]
yy=[]
pos=0

def posicion(event):
    global pos
    xx.append(event.x)
    yy.append(event.y)
    pos=pos+1
    lienzo.create_oval((event.x)-2,(event.y)-2,(event.x)+2,(event.y)+2, fill="green")


        
class circulo:    
    def operacion(self):
        diagonal=(math.sqrt((pow((xx[pos-2]-xx[pos-1]),2))+(pow((yy[pos-2]-yy[pos-1]),2)))) 
        radio=diagonal/2
        lienzo.create_oval(xx[pos-2],yy[pos-2],xx[pos-1], yy[pos-1],fill="grey")
        #lienzo.create_oval(xx[0]-(xx[0]/2), yy[0]-(yy[0]/2),xx[1], yy[1],fill="green")
        result1.set("Perimetro:"+str(2*math.pi*radio))
        result2.set("Area:"+str(math.pi*(pow(radio,2))))

class cuadrado:
        
    def operacion(self):
        lienzo.create_line(xx[pos-1], yy[pos-2],xx[pos-2], yy[pos-2],fill="red")
        lienzo.create_line(xx[pos-1], yy[pos-2],xx[pos-1], yy[pos-1],fill="red")
        lienzo.create_line(xx[pos-2], yy[pos-1],xx[pos-2], yy[pos-2],fill="red")
        lienzo.create_line(xx[pos-2], yy[pos-1],xx[pos-1], yy[pos-1],fill="red")
        result1.set("Perimetro:"+str((abs(xx[pos-2]-xx[pos-1])*2)+(abs(yy[pos-2]-yy[pos-1])*2)))
        result2.set("Area:"+str((xx[pos-2]-xx[pos-1])*(yy[pos-2]-yy[pos-1])))

class triangulo:
        
    def operacion(self):
        diagonal=(math.sqrt((pow((xx[pos-2]-xx[pos-1]),2))+(pow((yy[pos-2]-yy[pos-1]),2))))
        lienzo.create_line(xx[pos-2], yy[pos-2],xx[pos-1], yy[pos-1],fill="blue")
        lienzo.create_line(xx[pos-2], yy[pos-1],xx[pos-1], yy[pos-1],fill="blue")
        lienzo.create_line(xx[pos-2], yy[pos-1],xx[pos-2], yy[pos-2],fill="blue")
        result1.set("Perimetro:"+str(abs(xx[pos-2]-xx[pos-1])+abs(yy[pos-2]-yy[pos-1])+diagonal))
        result2.set("Area:"+str(((xx[pos-2]-xx[pos-1])*(yy[pos-2]-yy[pos-1]))/2))

class Figura(circulo, cuadrado, triangulo):
    
    def fcirculo(self):
        circulo.operacion(self)
    def fcuadrado(self):
        cuadrado.operacion(self)
    def ftriangulo(self):
        triangulo.operacion(self)

def dibujar():
    opcion = var.get()
    if opcion==1:
        obj.fcirculo()
        
    if opcion==2:
        obj.fcuadrado()
        
    if opcion==3:
        obj.ftriangulo()
       
marco=tk.Tk()
marco.title("Dibujo figuras")
marco.geometry("400x550")
marco.configure(background="white")
var= tk.IntVar()

obj= Figura()


b1 = tk.Radiobutton(marco,text ='Circulo' ,variable=var ,value=1)
b1.grid(row=1, column=0, sticky=tk.W)
b2 = tk.Radiobutton(marco,text ='Cuadrado' ,variable=var ,value=2)
b2.grid(row=2, column=0, sticky=tk.W)
b3 = tk.Radiobutton(marco,text ='Triangulo' ,variable=var ,value=3)
b3.grid(row=3, column=0, sticky=tk.W)


result1= tk.StringVar()
result2= tk.StringVar()

etiqueta1=tk.Label(marco, textvariable = result1)
etiqueta1.grid(row=5, column=0)

etiqueta2=tk.Label(marco, textvariable = result2)
etiqueta2.grid(row=6, column=0)

lienzo=Canvas(marco,width=400,height=400,background="grey")
lienzo.pack()
lienzo.place(x=0,y=150)
lienzo.bind("<Button-1>", posicion)



tk.Button(marco,text='Dibujar',command=dibujar).grid(row=4,column=0,sticky=tk.W,pady=4)

marco.mainloop()
    
