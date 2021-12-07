# Utilizamos módulo turtle para crear aplicaciones gráficas

import turtle

# Ahora crearemos una ventana, la cual tendrá un color, un título y unas ciertas dimensiones
ventana=turtle.Screen()
ventana=turtle.bgcolor("black")
ventana=turtle.title("Laberinto")
ventana=turtle.setup(700,700)

# Creamos una clase que nos permita dibujar los cuadros en la pantLLa, la cual será una subclase del módulo turtle, y la inicializamos

class lab(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)  #Después de inicializarla, le damos propiedades
        self.shape("square")
        self.color("white")
        self.penup()  #para que no deje rastro
        self.speed(0) #para que se pueda ver como se va dibujamdo

niveles=[]
#definir nivel
nivel_1=[
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
