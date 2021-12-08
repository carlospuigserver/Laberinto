# Laberinto
Dirección GitHub para este repositorio: https://github.com/carlospuigserver/Laberinto.git

Para este trabajo, he empleado el módulo turtle para poder emplear una interfaz gráfica, aunque desgraciadamente no he sabido ejecutar bien el programa, en el sentido de que no he sido capaz de que el personaje que he creado, pueda seguir un movimiento controlado por el usuario, pero lo que viene siendo el mapa y el personaje han sido creados correctamente.

El diagrama de flujo relacionado con el programa es el siguiente:








De todas maneras, aquí te adjunto el link por si no se ve del todo bien la imagen: https://www.figma.com/file/Gv20F83Rr3PDqdn2NqPo5j/Untitled?node-id=0%3A1




El código que he elaborado para poder realizar este programa es el siguiente:

```# Utilizamos módulo turtle para crear aplicaciones gráficas

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
    


#Creamos una clase para definir un jugador, la cual será una subclase del módulo turtle, y la inicializamos

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)  
        self.shape("circle")
        self.color("yellow")
        self.penup()  
        self.speed(0)
        self.goto(0,0) 
        self.direction="stop"







    
        

            
niveles=[]
#definir nivel
nivel_1=[
 
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX P                  XX",
"XXX      XXXXXXX   XXXXXX",
"XXX      XXX        XXXXX",
"XXX      XXX    XXXXXXXXX",
"XXX      XXX    XXXXXXXXX",
"XXX  XXXXXXX    XXXXXXXXX",
"XXX  XXXXXXX     XXXXXXXX",
"XXX  XXXXXXX    XXXXXXXXX",
"XXX  XXXXXXXXX        XXX",
"XXX  XXXXXXXXX        XXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX     XXXXXX",
"XXX  XXXXXXXXX     XXXXXX",
"XXX  XXXXXXXXX        XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXX                   XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXXXXXXXXXXXXXXXXXXXX XXX",

    
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
                if letra_x=="P":
                    player.goto(screen_x,screen_y)
            
            
            
            # Aquí estoy creando una secuancia para los movimientos
            while letra_x=="P":
                direccion="arriba" or "abajo" or "izquierda" or "derecha".format(direccion)
                if direccion=="arriba":
                    x=x
                    y=y+1
                if direccion=="abajo":
                    x=x
                    y=y-1
                if direccion=="izquierda":
                    x=x-1
                    y=y
                if direccion=="derecha":
                    x=x+1
                    y=y    
