# Utilizamos módulo turtle para crear aplicaciones gráficas

import turtle

# Ahora crearemos una ventana, la cual tendrá un color, un título y unas ciertas dimensiones
ventana=turtle.Screen()
ventana=turtle.bgcolor("black")
ventana=turtle.title("Laberinto")
ventana=turtle.setup(700,700)

# Creamos una clase que nos permita dibujar los cuadros en la pantLLa, la cual será una subclase del módulo turtle, y la inicializamos

class pen(turtle.Turtle):
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
    "XXXXXXXXXX       XXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXX             XXXXXXXX",
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
niveles.append(nivel_1)

#definir función para empezar a dibujar el laberinto
def iniciar_lab(nivel):
    for fila in range(len(nivel)):    
            for  column in range(len(nivel[fila])):   #Lo que estoy haciendo ahora es iterar cada uno de los elementos de la lista por filas y por columnas, y donde haya una "X", sustituirlo por un cuadrado
                letra_x=nivel[fila][column]
                screen_x=-288 + (column*24)
                screen_y=+288 - (fila*24)

                if letra_x=="X":
                    pen.goto(screen_x,screen_y)
                    pen.stamp()
                
                    

pen = pen()
                                                    
iniciar_lab(niveles[0])
