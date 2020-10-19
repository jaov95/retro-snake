#snake.py - Se recrea el juego snake con python
#Imports
import pygame
import random
import time
#<->

#Definicion de colores
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
#<->

#Definicion de superficie (ventana) y mensajes
ancho = 800
alto = 600

pygame.init()

superficie = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont(None, 25)
#<->

#Otras variables
reloj = pygame.time.Clock()
cuadro = 30

gameExit=False
#<->

#Definicion de variables para objetos del juego
snake_size = 10

listaSnake = []
largoSnake = 1

mover_x = 300
mover_y = 300

mover_x_cambio = 0
mover_y_cambio = 0

apple_size = 10
manzana_x_random = random.randrange(0, ancho -apple_size, apple_size)
manzana_y_random = random.randrange(0, alto -apple_size, apple_size)
#<->

#Funciones
def GameOverMessage(msg, color):
    pantalla_texto = font.render(msg, True, color)
    superficie.blit(pantalla_texto, [300,300])
    
def snake(snake_size, listaSnake):
    for i in listaSnake:
        #Dibuja la serpiente
        pygame.draw.rect(superficie, Negro, [i[0],i[1], snake_size, snake_size])
        
def puntaje(puntos):
    texto = font.render("Puntaje: "+str(puntos), True, Negro)
    superficie.blit(texto, [0,0])
#<->

#Ciclo de actualizacion del juego    
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit= True
        #<if>
    #<for>
            
    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mover_x_cambio = -10
            mover_y_cambio = 0
        #<if>
        if event.key == pygame.K_RIGHT:
            mover_x_cambio = 10
            mover_y_cambio = 0
        #<if>
        if event.key == pygame.K_UP:
            mover_x_cambio = 0
            mover_y_cambio = -10
        #<if>
        if event.key == pygame.K_DOWN:
            mover_x_cambio = 0
            mover_y_cambio = 10
        #<if>
    #<if>
            
    #Se establecen los limites de la superficie para la serpiente (bounds)
    if mover_x >= ancho or mover_x < 0 or mover_y >= alto or mover_y < 0:
        gameExit = True
    #<if>
        
    #Se asigna el cambio de movimiento para que este sea constante
    mover_y += mover_y_cambio
    mover_x += mover_x_cambio
    
    #Colorea la superficie (fondo)
    superficie.fill(Blanco)
    
    #Dibuja la manzana (cuadro rojo)
    pygame.draw.rect(superficie, Rojo, [manzana_x_random, manzana_y_random, apple_size, apple_size])

    #Se establece una cabeza para la serpiente
    cabezaSnake = []
    cabezaSnake.append(mover_x)
    cabezaSnake.append(mover_y)

    #Se agrega la cabeza al cuerpo de la serpiente
    listaSnake.append(cabezaSnake)
    
    #Se elimina el primer elemento para que la serpiente crezca y se mueva hacia adelante
    if len(listaSnake) > largoSnake:
        del listaSnake[0]
        
    #Se dibuja el cuerpo completo de la serpiente 
    snake(snake_size, listaSnake)

    #Se muestra el puntaje por cada manzana son 10 puntos
    puntaje(largoSnake-1)

    #Refresca la imagen en pantalla
    pygame.display.update()
    
    #Si la serpiente toca la manzana la manzana se dibuja en otro lugar y la serpiente crece 1 cuadrito
    if mover_x == manzana_x_random and mover_y == manzana_y_random:
        manzana_x_random = random.randrange(0, ancho - apple_size, apple_size)
        manzana_y_random = random.randrange(0, alto - apple_size, apple_size)
        largoSnake+=1
        
    #Se asigna un tick al reloj lo que regula la velocidad de movimiento
    reloj.tick(cuadro)
    
#<while>
#Fin del ciclo de actualizacion del juego
    
#Mensaje en caso de que la serpiente toque los bordes (game over)
GameOverMessage('Game Over', Rojo)
    
#Refresca la imagen en pantalla
pygame.display.update()
    
#Se generea una espera de 3 segundos (se muestra game over por 3 segundos)
time.sleep(3)
    
pygame.quit()
quit()
