#snake.py - Se recrea el juego snake con python
#<Imports>
import pygame
import random
import time
#<->
pygame.init()
#<Definicion de colores>
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Verde = (0, 150, 0)
#<->

#<Definicion de superficie (ventana), texto e imagenes>
ancho = 800
alto = 600

icono = pygame.image.load("iconRetroSnakeG64.png")
pygame.display.set_icon(icono)
superficie = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Retro Snake')

font = pygame.font.Font("arcadeclassic.ttf", 25)

logoIntro = pygame.image.load("logoIconRetroSnake100x100.png")
#<->

#<Definicion de constantes para objetos del juego>
snake_size = 10
apple_size = 10
#<->

#<Definicion de sonidos y musica>
reproducirMusica = pygame.mixer.Sound("SongOfSnake.ogg")
reproducirMusica.set_volume(0.50)

gameOverSound = pygame.mixer.Sound("GameOverSnake.ogg")
gameOverSound.set_volume(0.50)

pauseOn = pygame.mixer.Sound("PauseOnSnake.ogg")
pauseOn.set_volume(0.70)

pauseOff = pygame.mixer.Sound("PauseOffSnake.ogg")
pauseOff.set_volume(0.70)

snakeBite = pygame.mixer.Sound("BeepSnake.ogg")
snakeBite.set_volume(0.70)
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
def snake(snake_size, listaSnake, color):
    for i in listaSnake:
        #Dibuja la serpiente
        pygame.draw.rect(superficie, color, [i[0],i[1], snake_size, snake_size])
#<snake()>
        
#Muestra el puntaje en pantalla de manera constante    
def puntaje(puntos, color):
    texto = font.render("Puntaje "+str(puntos), True, color)
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
        superficie.fill(Negro)
        screenMessage("Juego Pausado", Blanco, ancho, alto, 0)
        screenMessage("Presion  C  para continuar o  Q  para salir del juego", Verde, ancho, alto, 150)
        pygame.display.update()
        reloj.tick(cuadro)
    #<while>
#<pausa()>
        
def gameIntro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #<if>
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                #<if>
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                #<elif>
            #<if>
        #<for>
        superficie.fill(Negro)
        superficie.blit(logoIntro, [350,80])
        screenMessage("Retro Snake",Verde, ancho, alto, -100)
        screenMessage("Mueve  la  serpiente  con  las  flechas  de  tu  teclado",Blanco, ancho, alto, 100)
        screenMessage("Come  todas  las  manzanas  que  puedas",Blanco, ancho, alto, 130)
        screenMessage("No  toques  los  bordes  y  cuidado  con  morder  tu  propio  cuerpo",Blanco, ancho, alto, 160)
        screenMessage("Presiona  C  para  comenzar  o  Q  para  salir",Verde, ancho, alto, 220)
        pygame.display.update()
        reloj.tick(cuadro)
#<gameIntro()>
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

    reproducirMusica.play(-1)
    
    #Ciclo de actualizacion del juego en partida  
    while not gameExit:        
        
        
        if gameOver==True:
            reproducirMusica.stop()
            gameOverSound.play()
        #Game Over Screen que permite ejecutar nuevamente el juego o salir   
        while gameOver == True:
            superficie.fill(Negro)
            screenMessage("Game Over", Rojo, ancho, alto, 0)
            screenMessage("Presiona C para reintentarlo Q para salir", Verde, ancho, alto, 150)
            screenMessage("Presiona R para volver al menu principal", Verde, ancho, alto, 180)
            pygame.display.update()
            #Segun la tecla que presione el jugador el gameLoop se ejecuta nuevamente o sale de la aplicacion
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        gameLoop()
                    elif event.key == pygame.K_r:
                        gameOver=False
                        gameExit=False
                        gameIntro()
                        gameLoop()
            #<for>
        #<while>
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit= True
            #<if>
            if event.type==pygame.KEYDOWN:
                #Cambia la direccion segun la tecla presionada
                if event.key == pygame.K_LEFT:
                    mover_y_cambio = 0
                    if mover_x_cambio != snake_size:
                        mover_x_cambio = -snake_size
                        mover_y_cambio = 0
                    #<if>
                #<if>
                elif event.key == pygame.K_RIGHT:
                    mover_y_cambio = 0
                    if mover_x_cambio !=-snake_size:
                        mover_x_cambio = snake_size
                        mover_y_cambio = 0
                #<if>
                elif event.key == pygame.K_UP:
                    mover_x_cambio = 0
                    if mover_y_cambio != snake_size:
                        mover_y_cambio = -snake_size
                        mover_x_cambio = 0
                #<if>
                elif event.key == pygame.K_DOWN:
                    mover_x_cambio = 0
                    if mover_y_cambio !=-snake_size:
                        mover_y_cambio = snake_size
                        mover_x_cambio = 0
                #<if>
                elif event.key == pygame.K_p:
                    reproducirMusica.set_volume(0.0)
                    pauseOn.play()
                    pausa()
                    pauseOff.play()
                    reproducirMusica.set_volume(0.50)
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
        superficie.fill(Negro)
        
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
        snake(snake_size, listaSnake, Verde)

        #Se muestra el puntaje por cada manzana son 10 puntos
        puntaje((largoSnake-1)*10, Verde)

        #Refresca la imagen en pantalla
        pygame.display.update()
        
        #Si la serpiente toca la manzana la manzana se dibuja en otro lugar y la serpiente crece 1 cuadrito
        if mover_x == manzana_x_random and mover_y == manzana_y_random:
            snakeBite.play()
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
gameIntro()
gameLoop()
