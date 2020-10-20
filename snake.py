#snake.py - Se recrea el juego snake con python
#<Imports>
import pygame
import random
import time
#<->

#<Definicion de colores>
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
#<->

#<Definicion de superficie (ventana) y mensajes>
ancho = 800
alto = 600

pygame.init()

superficie = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont(None, 25)
#<->

#<Definicion de constantes para objetos del juego>
snake_size = 10
apple_size = 10
#<->

#<Otras constantes>
reloj = pygame.time.Clock()
cuadro = 30
#<->

#<Funciones>
#Crea un texto y lo retorna 
def textObject(msg, color):
    texto_superficie = font.render(msg, True, color)
    return texto_superficie, texto_superficie.get_rect()
#<textObject()>

#Muestra el mensaje deseado en pantalla como otro screen
def screenMessage(msg, color, x, y, offset_y):
    texto, texto_centrado = textObject(msg, color)
    texto_centrado.center = (x//2),(y//2)+offset_y
    superficie.blit(texto, texto_centrado)
#<screenMessage()>
    
#Dibuja la serpiente   
def snake(snake_size, listaSnake):
    for i in listaSnake:
        #Dibuja la serpiente
        pygame.draw.rect(superficie, Negro, [i[0],i[1], snake_size, snake_size])
#<snake()>
        
#Muestra el puntaje en pantalla de manera constante    
def puntaje(puntos):
    texto = font.render("Puntaje: "+str(puntos), True, Negro)
    superficie.blit(texto, [0,0])
#<puntaje()>
    
#Pausa el juego y muestra un mensaje en pantalla
def pausa():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #<if>
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                #<if>
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                #<elif>
            #<if>
        #<for>
        superficie.fill(Blanco)
        screenMessage("Juego Pausado", Negro, ancho, alto, 0)
        screenMessage("Presion \"c\" para continuar o \"q\" para salir del juego", Negro, ancho, alto, 150)
        pygame.display.update()
        reloj.tick(15)
    #<while>
#<->

#Ciclo del juego completo
def gameLoop():
    gameExit = False
    gameOver = False

    mover_x = 300
    mover_y = 300
    mover_x_cambio = 0
    mover_y_cambio = 0
    
    listaSnake = []
    largoSnake = 1

    manzana_x_random = random.randrange(0, ancho -apple_size, apple_size)
    manzana_y_random = random.randrange(0, alto -apple_size, apple_size)
    
    #Ciclo de actualizacion del juego    
    while not gameExit:
        #Game Over Screen que permite ejecutar nuevamente el juego o salir
        while gameOver == True:
            superficie.fill(Blanco)
            screenMessage("Game Over", Rojo, ancho, alto, 0)
            screenMessage("Presiona \"c\" para reintentarlo o \"q\" para salir", Negro, ancho, alto, 150)
            pygame.display.update()
            #Segun la tecla que presione el jugador el gameLoop se ejecuta nuevamente o sale de la aplicacion
            for event in pygame.event.get():
                if event.key == pygame.K_q:
                    gameExit = True
                    gameOver = False
                if event.key == pygame.K_c:
                    gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit= True
            #<if>
        
            #Cambia la direccion segun la tecla presionada       
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -10
                    mover_y_cambio = 0
                #<if>
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = 10
                    mover_y_cambio = 0
                #<if>
                elif event.key == pygame.K_UP:
                    mover_x_cambio = 0
                    mover_y_cambio = -10
                #<if>
                elif event.key == pygame.K_DOWN:
                    mover_x_cambio = 0
                    mover_y_cambio = 10
                #<if>
                elif event.key == pygame.K_p:
                    pausa()
            #<if>
        #<for>
                    
        #Se establecen los limites de la superficie para la serpiente (bounds)
        if mover_x >= ancho or mover_x < 0 or mover_y >= alto or mover_y < 0:
            gameOver = True
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
            
        #Cuando la cabezaSnake se posiciona en un elemento de cuerpoSnake gameOver es True
        for eachSegment in listaSnake[:-1]:
            if eachSegment == cabezaSnake:
                gameOver = True
          
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
    screenMessage('Game Over', Rojo, ancho, alto, 0)
        
    #Refresca la imagen en pantalla
    pygame.display.update()
        
    #Se generea una espera de 3 segundos (se muestra game over por 3 segundos)
    time.sleep(3)
        
    pygame.quit()
    quit()
#<gameLoop()>
gameLoop()
