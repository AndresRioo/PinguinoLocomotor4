
import pygame
import random
import asyncio

# METODO INICIAR

import pygame

def rectangulo(width,height):
    # Configuración del rectangulo
    rectangulo_width, rectangulo_height = 50, 50 # tamaño
    rectangulo_color = (255, 0, 0)  # color
    rectangulo_x, rectangulo_y = 675, 1150 # posicion
    rectangulo_rect = pygame.Rect(rectangulo_x, rectangulo_y, rectangulo_width, rectangulo_height)  # rect del rectangulo

    return (rectangulo_color,rectangulo_rect)


def pinguinoCrear(startx,starty):
    pinguino = pygame.image.load(r"fotosPython\pingu.png")
    #pinguino = pygame.image.load(r"C:\Users\rioan\OneDrive\Escritorio\PyGey\.venv\fotosPython\pinguion.png")
    pinguino = pygame.transform.flip( pinguino, False, True)  #invertir la imagen (que mire a la derecha y no izquierda)
    pinguino = pygame.transform.rotate(pinguino, 180)

    pinguino_rect = pinguino.get_rect()
    pinguino_rect.center = (startx,starty)  # Posición inicial del objeto

    nueva_escala = 0.15  # Cambia este valor según lo pequeña que quieras la imagen
    pinguino = pygame.transform.scale(pinguino, (int(pinguino_rect.width * nueva_escala), int(pinguino_rect.height * nueva_escala)))

    pinguino_rect = pinguino.get_rect()
    pinguino_rect.center = (startx, starty)  # Posición inicial del objeto

    return (pinguino,pinguino_rect)


#Suelo con el canvas (misma escala)
def sueloNormal(width, height , posicionx, posiciony ,imagen):
    #Width y height indican la posicion a poner
    #La posicionx ayuda a ponerlos todos en fila ( + distancia para ponerlo junto a otro conjunto de bloques)
    #La posiciony ayuda a ponerlos todos en pila 
    #La imagen elige la imagen

    #0 la verde , 1 la azul, 2 la rosa , 3 pincho azul, 4 pincho rosa
    urlList = [r"fotosPython\bloque basico.png" , r"fotosPython\SueloAzul.png", r"fotosPython\SueloRosa.png", r"fotosPython\pinchoAzul.png", r"fotosPython\pinchoRosa.png" ]

    # SUELO
    # Configuración del suelo
    sueloAzul = pygame.image.load(urlList[imagen])
    #print("se ha usado la foto ",j ," que es :", urlList[j])
    #sueloAzul = pygame.transform.flip( sueloAzul, False, True)  #invertir la imagen (que mire a la derecha y no izquierda)
    sueloAzul = pygame.transform.rotate(sueloAzul, 90)

    sueloAzul_rect = sueloAzul.get_rect()
    sueloAzul_rect.center = ( width, height)  # Posición inicial del objeto

    nueva_escala = 0.10  # Cambia este valor según lo pequeña que quieras la imagen
    sueloAzul = pygame.transform.scale(sueloAzul, (int(sueloAzul_rect.width * nueva_escala), int(sueloAzul_rect.height * nueva_escala)))

    sueloAzul_rect = sueloAzul.get_rect()

    W = width + posicionx*sueloAzul.get_size()[0]
    H = height + posiciony*sueloAzul.get_size()[1]

    sueloAzul_rect.center = ( W, H)  # Posición inicial del objeto

    #util para saber el tamaño y poder colocarlos juntos :)
    #print(sueloAzul.get_size())

    return (sueloAzul,sueloAzul_rect, W , H )

#suelo del pixelart a otra escala
def sueloRaya(width, height,posicionx,posiciony,imagen):
    #Width y height indican la posicion a poner
    #La posicionx ayuda a ponerlos todos en fila ( + distancia para ponerlo junto a otro conjunto de bloques)
    #La posiciony ayuda a ponerlos todos en pila 
    #La imagen elige la imagen

    # 0 la verde (no deberia) , 1 suelo azul a rayas, 2 suelo rosa a rayas 3 pincho azul raya, 4 pincho rosa raya, 5 pincho azul normal 6 pincho rosa normal
    urlList = [KeyError,r"fotosPython\sueloAzulnt.png", r"fotosPython\sueloRojont.png", r"fotosPython\pinchoAzulnt.png", r"fotosPython\pinchoRojont.png", r"fotosPython\pincho.png", r"fotosPython\pincho rojo normal.png"]

    # SUELO
    # Configuración del suelo
    sueloAzul = pygame.image.load(urlList[imagen])
    #print("se ha usado la foto ",j ," que es :", urlList[j])
    #sueloAzul = pygame.transform.flip( sueloAzul, False, True)  #invertir la imagen (que mire a la derecha y no izquierda)
    sueloAzul = pygame.transform.rotate(sueloAzul, 90)

    sueloAzul_rect = sueloAzul.get_rect()
    sueloAzul_rect.center = ( width, height)  # Posición inicial del objeto

    nueva_escala = 0.5  # Cambia este valor según lo pequeña que quieras la imagen
    sueloAzul = pygame.transform.scale(sueloAzul, (int(sueloAzul_rect.width * nueva_escala), int(sueloAzul_rect.height * nueva_escala)))

    sueloAzul_rect = sueloAzul.get_rect()
    W = width + posicionx*sueloAzul.get_size()[0]
    H = height + posiciony*sueloAzul.get_size()[1]

    sueloAzul_rect.center = ( W, H)  # Posición inicial del objeto
    #util para saber el tamaño y poder colocarlos juntos :)
    #print(sueloAzul.get_size())

    return (sueloAzul,sueloAzul_rect,  W,H)


def Pinchos(width, height,posicionx,posiciony,imagen,rotacion):
    #Width y height indican la posicion a poner
    #La posicionx ayuda a ponerlos todos en fila ( + distancia para ponerlo junto a otro conjunto de bloques)
    #La posiciony ayuda a ponerlos todos en pila 
    #La imagen elige la imagen

    # url + escala

    # 0 pincho azul raya, 1 pincho rosa raya, 2 pincho azul normal 3 pincho rosa normal
    urlList = [ r"fotosPython\pinchoAzulnt.png", r"fotosPython\pinchoRojont.png", r"fotosPython\pincho.png", r"fotosPython\pincho rojo normal.png"]
    
    # SUELO
    # Configuración del suelo
    sueloAzul = pygame.image.load(urlList[imagen])
    #print("se ha usado la foto ",j ," que es :", urlList[j])
    #sueloAzul = pygame.transform.flip( sueloAzul, False, True)  #invertir la imagen (que mire a la derecha y no izquierda)
    sueloAzul = pygame.transform.rotate(sueloAzul, 90 + 90*rotacion)

    sueloAzul_rect = sueloAzul.get_rect()
    sueloAzul_rect.center = ( width, height)  # Posición inicial del objeto

    nueva_escala = 0.5  # Cambia este valor según lo pequeña que quieras la imagen
    sueloAzul = pygame.transform.scale(sueloAzul, (int(sueloAzul_rect.width * nueva_escala), int(sueloAzul_rect.height * nueva_escala)))

    sueloAzul_rect = sueloAzul.get_rect()
    W = width + posicionx*sueloAzul.get_size()[0]
    H = height + posiciony*sueloAzul.get_size()[1]

    sueloAzul_rect.center = ( W, H)  # Posición inicial del objeto
    #util para saber el tamaño y poder colocarlos juntos :)
    #print(sueloAzul.get_size())

    return (sueloAzul,sueloAzul_rect,  W,H, rotacion)


def ObjetosRandom(width, height,posicionx,posiciony,imagen):
    #Width y height indican la posicion a poner
    #La posicionx ayuda a ponerlos todos en fila ( + distancia para ponerlo junto a otro conjunto de bloques)
    #La posiciony ayuda a ponerlos todos en pila 
    #La imagen elige la imagen

    # url + escala

    # 0 de salir , 1 de sexo png , 2 de UB , 3 de empezar 
    urlList = [ (r"fotosPython\salir.png", 2 ) , (r"fotosPython\sexo.png", 2), (r"fotosPython\dale a la v.png",4), (r"fotosPython\empezar.png",2) ]

    # SUELO
    # Configuración del suelo
    sueloAzul = pygame.image.load(urlList[imagen][0])
    #print("se ha usado la foto ",j ," que es :", urlList[j])
    #sueloAzul = pygame.transform.flip( sueloAzul, False, True)  #invertir la imagen (que mire a la derecha y no izquierda)
    sueloAzul = pygame.transform.rotate(sueloAzul, 0)

    sueloAzul_rect = sueloAzul.get_rect()
    sueloAzul_rect.center = ( width, height )  # Posición inicial del objeto

    nueva_escala = urlList[imagen][1]  # Cambia este valor según lo pequeña que quieras la imagen
    sueloAzul = pygame.transform.scale(sueloAzul, (int(sueloAzul_rect.width * nueva_escala), int(sueloAzul_rect.height * nueva_escala)))

    sueloAzul_rect = sueloAzul.get_rect()
    W = width + posicionx*sueloAzul.get_size()[0]
    H = height + posiciony*sueloAzul.get_size()[1]

    sueloAzul_rect.center = ( W, H)  # Posición inicial del objeto
    #util para saber el tamaño y poder colocarlos juntos :)
    #print(sueloAzul.get_size())

    return (sueloAzul,sueloAzul_rect,  W,H)
































# METODO BLOQUES 

import pygame

def Bloques(width, height , posicionx, posiciony , tipo , estado=None , rotacion=None, fliping=None ):
    #Width y height indican la posicion a poner
    #La posicionx ayuda a ponerlos todos en fila ( + distancia para ponerlo junto a otro conjunto de bloques)
    #La posiciony ayuda a ponerlos todos en pila 
    #Tipo - string con el bloque deseado
    #Estado indica si activo o inactivo
    #Rotacion para rotarlo (pinchos)

    imagen = -1
    escala = -1
    
    if tipo == "BloqueVerde":

        imagen = r"fotosPython\bloque basico.png"
        escala = 0.10
    
    if tipo == "PinchoVerde":

        imagen = r"fotosPython\pincho verde.png"
        escala = 0.50

    if tipo == "BloqueAzul":

        if estado == 1:

            imagen = r"fotosPython\SueloAzul.png"
            escala = 0.10

        elif estado == 0:

            imagen = r"fotosPython\sueloAzulnt.png"
            escala = 0.50
    
    if tipo == "BloqueRosa":

        if estado == 1:

            imagen = r"fotosPython\SueloRosa.png"
            escala = 0.10

        elif estado == 0:

            imagen = r"fotosPython\sueloRojont.png"
            escala = 0.50
    
    if tipo == "PinchoAzul":

        if estado == 1:

            imagen = r"fotosPython\pincho.png"
            escala = 0.50

        elif estado == 0:

            imagen = r"fotosPython\pinchoAzulnt.png"
            escala = 0.50
    
    if tipo == "PinchoRosa":

        if estado == 1:

            imagen = r"fotosPython\pincho rojo normal.png"
            escala = 0.50

        elif estado == 0:

            imagen = r"fotosPython\pinchoRojont.png"
            escala = 0.50


    if imagen == -1:
        print("IMAGEN INCORRECTA")
        return NameError


    if fliping == None:
        #print("donete")
        fliping = (False,False)
    
    if rotacion == None:
        #print("done donete")
        rotacion = 0


    # Configuración del sprite
    Sprite = pygame.image.load(imagen)
    #print("se ha usado la foto ",j ," que es :", urlList[j])

    Sprite = pygame.transform.flip( Sprite, fliping[0] , fliping[1])  #invertir la imagen (que mire a la derecha y no izquierda)
    Sprite = pygame.transform.rotate(Sprite, rotacion)

    Sprite_rect = Sprite.get_rect()
    Sprite_rect.center = ( width, height)  # Posición inicial del objeto

    Sprite = pygame.transform.scale(Sprite, (int(Sprite_rect.width * escala), int(Sprite_rect.height * escala)))

    Sprite_rect = Sprite.get_rect()

    W = width + posicionx*Sprite.get_size()[0]
    H = height + posiciony*Sprite.get_size()[1]

    Sprite_rect.center = (W, H)  # Posición inicial del objeto

    #util para saber el tamaño y poder colocarlos juntos :)
    #print(sueloAzul.get_size())

    return (Sprite,Sprite_rect, W , H, tipo, estado, rotacion, fliping )










#MENU
def MENU():

    pygame.init()

    # Configuración de la ventana
    width, height = 1000, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pinguino Locomotor 4")



    # Cargar imagen de fondo
    fondo = pygame.image.load(r"fotosPython\frames\frame 1\frame 1 negro.bmp")
    #fondo = pygame.transform.scale(fondo, (width, height))



    # OBJETOS EN PANTALLA


    #PUNTUACION MAXIMA

    font_path = r"fotosPython\Comic Sans MS.ttf"  #COMIC SANS SIUUUUUUUUUUUUUUU (hola)
    # Definir el tamaño de la fuente
    font_size = 36
    #Cargar la fuente TrueType
    font = pygame.font.Font(font_path, font_size)

    with open(r"fotosPython\score.txt.txt", 'r+') as file:
                # Lee todo el contenido del archivo en una cadena
                contenido = file.read()
                contenido = int(contenido)

    Joder = "Puntuacion maxima : " + "" + str(contenido) 
    text_surface = font.render( Joder , True, (0, 255, 0))
    scorex = 100
    scorey = 700
    


    # RECTANGULO
    rectangulo_color, rectangulo_rect = rectangulo(width,height)

    #PINGUINO
    spawnx = 450     #90
    spawny = 500    #200
    pinguino, pinguino_rect = pinguinoCrear(spawnx,spawny)
    direccion_derecha = True  # Indica la dirección actual del pingüino

    #SUELOS

    # COORDENADAS DEL SUELO FIJO Y --- 600
    # DISTANCIA INDICA LOS BLOQUES DE DIFERENCIA
    # SI QUIERO PONERLOS EN FILA sueloNormal(x,x, distancia, 0, x)
    # SI QUIERO PONERLOS EN COLUMNA sueloRaya(x,x,0 ,distancia,x)                 


    # SUELO VERDE
    spawnx = 000     #50
    spawny = 600    #600
    numBlocsVerds = 21
    sueloVerdeList = []

    for i in range(numBlocsVerds):
        #sueloVerde, sueloVerde_rect = iniciar.sueloVerde(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloVerde, sueloVerde_rect, xxx, xxxx = sueloNormal(spawnx,spawny,i,0,0) # 0 de verde
        sueloVerdeList.append((sueloVerde,sueloVerde_rect))

    distanciaX = numBlocsVerds



    # SUELO AZUL
    PosicionInicial = 300

    spawnx = PosicionInicial     
    spawny = 400    #600
    distancia = 0   # numblocs
    numBlocsAzules = 5
    sueloAzulList = []
    for i in range(numBlocsAzules):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloAzul, sueloAzul_rect , posicionXBloque, posicionYBloque = sueloNormal(spawnx,spawny,i+distancia,0,1) # 1 de azul
        sueloAzulList.append([sueloAzul,sueloAzul_rect,1, posicionXBloque, posicionYBloque]) # el 1 indica que esta encendido

    numBlocsAzulesTotal = numBlocsAzules


    # SUELO ROJO
    spawnx = PosicionInicial     
    spawny = 400    #600
    distancia = numBlocsAzules   # numblocs  (apareceran despues a eso)
    numBlocsRojos = 5
    sueloRojoList = []
    for i in range(numBlocsRojos):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloRojo, sueloRojo_rect , posicionXBloque, posicionYBloque = sueloRaya(spawnx, spawny,i+distancia,0,2) # 2 de rojo
        sueloRojoList.append([sueloRojo,sueloRojo_rect, 0, posicionXBloque, posicionYBloque]) # el 0 indica que esta apagado

    numBlocsRojosTotal = numBlocsRojos



    #BLOQUES DE ARRIBA EXTRA

    # SUELO AZUL
    PosicionInicial = 000

    spawnx = PosicionInicial     
    spawny = 200    #600
    distancia = 0   # numblocs
    numBlocsAzules = 5
    for i in range(numBlocsAzules):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloAzul, sueloAzul_rect , posicionXBloque, posicionYBloque = sueloNormal(spawnx,spawny,i+distancia,0,1) # 1 de azul
        sueloAzulList.append([sueloAzul,sueloAzul_rect,1, posicionXBloque, posicionYBloque]) # el 1 indica que esta encendido

    numBlocsAzulesTotal += numBlocsAzules


    # SUELO ROJO
    spawnx = 600     
    spawny = 200    #600
    distancia = numBlocsAzules   # numblocs  (apareceran despues a eso)
    numBlocsRojos = 5
    for i in range(numBlocsRojos):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloRojo, sueloRojo_rect , posicionXBloque, posicionYBloque = sueloRaya(spawnx, spawny,i+distancia,0,2) # 2 de rojo
        sueloRojoList.append([sueloRojo,sueloRojo_rect, 0, posicionXBloque, posicionYBloque]) # el 0 indica que esta apagado

    numBlocsRojosTotal += numBlocsRojos


    #PRUEBA PINCHOS

    spawnx = 450     #50
    spawny = 350    #600
    distancia = 0   # numblocs
    numPinchosRojos = 2
    sueloPinchoRojoList = []
    for i in range(numPinchosRojos):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloRojo, sueloRojo_rect , posicionXBloque, posicionYBloque, rotacion = Pinchos(spawnx, spawny,i+distancia,0,1,2) # 4 de rosa pincho raya
        sueloPinchoRojoList.append([sueloRojo,sueloRojo_rect, 0, posicionXBloque, posicionYBloque, rotacion]) # el 0 indica que esta apagado

    numPinchosRojosTotal = numPinchosRojos 

    spawnx = 450     #50
    spawny = 350    #600
    distancia = numPinchosRojos   # numblocs
    numPinchosAzules = 2
    sueloPinchoAzulList = []
    for i in range(numPinchosAzules):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloAzul, sueloAzul_rect , posicionXBloque, posicionYBloque, rotacion = Pinchos(spawnx,spawny,i+distancia,0,2,2) # 5 de azul pincho normal
        sueloPinchoAzulList.append([sueloAzul,sueloAzul_rect,1, posicionXBloque, posicionYBloque, rotacion]) # el 1 indica que esta encendido

    numPinchosAzulesTotal = numPinchosAzules

    

    numPinchosTotal = numPinchosAzulesTotal + numPinchosRojosTotal


    # OBJETO RANDOM

    #SALIR
    spawnx = 100
    spawny = 100

    salir, salir_rect , salirposicionXBloque, salirposicionYBloque = ObjetosRandom(spawnx,spawny,0,0,0) # 0 de salir
    salirInfo = (salir,salir_rect,salirposicionXBloque,salirposicionYBloque)

    #SEXO
    spawnx = 900
    spawny = 100

    salir, salir_rect , salirposicionXBloque, salirposicionYBloque = ObjetosRandom(spawnx,spawny,0,0,1) # 1 de sexo
    sexoInfo = (salir,salir_rect,salirposicionXBloque,salirposicionYBloque)

    #EMPEZAR
    spawnx = 700
    spawny = 300

    empezar, empezar_rect , empezarposicionXBloque, empezarposicionYBloque = ObjetosRandom(spawnx,spawny,0,0,3) # 1 de sexo
    empezarInfo = (empezar,empezar_rect,empezarposicionXBloque,empezarposicionYBloque)



    # Bloques columna 

    spawnx = 200     #50
    spawny = 550    #600
    #distanciaY = 0   # numblocs
    numBlocsAzules = 8
    for i in range(numBlocsAzules):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloAzul, sueloAzul_rect , posicionXBloque, posicionYBloque = sueloNormal(spawnx,spawny,       0,-i,1) # 1 de azul
        sueloAzulList.append([sueloAzul,sueloAzul_rect,1, posicionXBloque, posicionYBloque]) # el 1 indica que esta encendido

    numBlocsAzulesTotal += numBlocsAzules

    spawnx = 850     #50
    spawny = 550    #600
    #distancia = 1 + 5   # bloques de distancia
    numBlocsRojos = 8
    for i in range(numBlocsRojos):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloRojo, sueloRojo_rect , posicionXBloque, posicionYBloque = sueloRaya(spawnx,spawny,      0,-i,2) # 2 de rojo
        sueloRojoList.append([sueloRojo,sueloRojo_rect, 0, posicionXBloque, posicionYBloque]) # el 0 indica que esta apagado

    numBlocsRojosTotal += numBlocsRojos


    # Bloques FILA 

    spawnx = 50     #50
    spawny = 600    #600
    numBlocsAzules = 0
    for i in range(numBlocsAzules):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloAzul, sueloAzul_rect , posicionXBloque, posicionYBloque = sueloNormal(spawnx,spawny,i + distanciaX,0,1) # 1 de azul
        sueloAzulList.append([sueloAzul,sueloAzul_rect,1, posicionXBloque, posicionYBloque]) # el 1 indica que esta encendido

    distanciaX += numBlocsAzules   # numblocs
    numBlocsAzulesTotal += numBlocsAzules

    spawnx = 50     #50
    spawny = 600    #600   
    numBlocsRojos = 0
    for i in range(numBlocsRojos):
        #sueloAzul, sueloAzul_rect = iniciar.sueloAzul(spawnx+i*75,spawny) # hacer con 75 hace que escalarlo requiera mas cambios
        sueloRojo, sueloRojo_rect , posicionXBloque, posicionYBloque = sueloRaya(spawnx, spawny,i + distanciaX,0,2) # 2 de rojo
        sueloRojoList.append([sueloRojo,sueloRojo_rect, 0, posicionXBloque, posicionYBloque]) # el 0 indica que esta apagado

    distanciaX += numBlocsRojos # bloques de distancia
    numBlocsRojosTotal += numBlocsRojos








    # TODA LA INFORMACION VARIABLE 

    numBlocsColoradosTotalList = sueloAzulList + sueloRojoList
    numBlocsColoradosTotal = numBlocsRojosTotal +  + numBlocsAzulesTotal




    #VELOCIDAD DE MOVIMIENTO
    velocidad = 1

    #Desaparecer Objetos
    rip = False

    # Ajustes de gravedad y salto
    gravedad = 1
    velocidad_salto = -3
    velocidad_y = 1
    en_suelo = False
    salto_en_curso = False
    contador_salto = 0

    #Habilitar movimiento horizontal ??? me gusta el pistacho
    porque_si = False

    #Habilitar movimiento bloques
    start = False

    #Presionar v para cambiar estado (1 vez por presion de tecla)
    v_presionada = False

    #Pinguino se muere
    boom = False

    # Bucle principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False


            elif event.type == pygame.KEYDOWN: #presionar la tecla

                if event.key == pygame.K_UP and en_suelo:
                    # Iniciar el salto si estamos en el suelo

                    velocidad_y = -3 #direccion contraria
                    en_suelo = False
                    salto_en_curso = True
                    altura = -4
                    contador_salto = 0

            elif event.type == pygame.KEYUP: #dejar de presionar la tecla

                if event.key == pygame.K_UP and salto_en_curso:
                    # Detener el salto si se libera la tecla de salto
                    salto_en_curso = False

                if event.key == pygame.K_v:
                    v_presionada = False
            



        #print(pygame.mouse.get_pos())
        
        
        #velocidad negativa sube 
        if salto_en_curso:

            pinguino_rect.y += altura
            contador_salto += 1

            if contador_salto >= 5: #5 saltos con -4 de movimiento
                altura = -3
            
            if contador_salto >= 12: # 7 saltos con -3 de movimiento
                altura = -2

            if contador_salto >= 62: # 20 saltos con -2 de movimiento
                altura = -1

            if contador_salto >= 222 : # 40 saltos con -1 de movimiento
                altura = 0

            #print(pinguino_rect.y, altura, contador_salto)

            if contador_salto >=500:
                salto_en_curso = False
        
        else:
            #gravedad
            velocidad_y += gravedad # siempre caera a velocidad maxima de 1

            if velocidad_y >= 2:
                velocidad_y = 1

            pinguino_rect.y += velocidad_y #subir cada vez mas lento y bajar

























        if boom:
            return 2








        # MOVIMIENTO DE LOS BLOQUES


        teclas = pygame.key.get_pressed()
        porque_si = True

        """
        if teclas[pygame.K_SPACE]:
            if not start:
                ultimo_movimiento = pygame.time.get_ticks()
            start = False

        if teclas[pygame.K_c]:
            porque_si = True
        
        if start:


            
            velocidadBloque = 2

            tiempo_entre_movimientos = 5  # Tiempo en milisegundos
            ahora = pygame.time.get_ticks()

            if ahora - ultimo_movimiento > tiempo_entre_movimientos:

                ultimo_movimiento = ahora

                for i in range(numBlocsVerds):
                    sueloVerdeList[i][1].x -= velocidadBloque


                for i in range(numBlocsAzulesTotal):
                    sueloAzulList[i][1].x -= velocidadBloque  #los bloques se mueven y actualizo la posicion x del rectangulo
                    sueloAzulList[i] = list(sueloAzulList[i])
                    sueloAzulList[i][3] -= velocidadBloque
                    
                for i in range(numBlocsRojosTotal):
                    sueloRojoList[i][1].x -= velocidadBloque  #los bloques se mueven y actualizo la posicion x del rectangulo
                    sueloRojoList[i] = list(sueloRojoList[i])
                    sueloRojoList[i][3] -= velocidadBloque
                
                for i in range(numPinchosAzulesTotal):
                    sueloPinchoAzulList[i][1].x -= velocidadBloque  #los bloques se mueven y actualizo la posicion x del rectangulo
                    sueloPinchoAzulList[i] = list(sueloPinchoAzulList[i])
                    sueloPinchoAzulList[i][3] -= velocidadBloque
                    
                for i in range(numPinchosRojosTotal):
                    sueloPinchoRojoList[i][1].x -= velocidadBloque  #los bloques se mueven y actualizo la posicion x del rectangulo
                    sueloPinchoRojoList[i] = list(sueloPinchoRojoList[i])
                    sueloPinchoRojoList[i][3] -= velocidadBloque
                    


                    #print(sueloAzulList[i])
                    #print(sueloAzulList[i][3])
                    #sueloAzulList[i] = list(sueloAzulList[i])   # por algun motivo se transforma a tupla ??
                    #sueloAzulList[i][3] = 2
                    #sueloAzulList[i][3] = sueloAzulList[i][1].x

        """
































        # CAMBIO EN LOS BLOQUES
                
        if teclas[pygame.K_v] and not v_presionada :

            v_presionada = True
            en_suelo = False

            #BLOQUES AZULES
            for i in range (numBlocsAzulesTotal):

                if sueloAzulList[i][2] == 1: # esta activo --> lo pasamos a raya
                
                    spawnx, spawny = sueloAzulList[i][3], sueloAzulList[i][4]

                    cambioAzulRaya, cambioAzulRaya_rect, posicionXBloque, posicionYBloque = sueloRaya(spawnx,spawny,0,0,1) # 1 de azul
                    sueloAzulList[i] = (cambioAzulRaya,cambioAzulRaya_rect, 0, posicionXBloque, posicionYBloque)

                elif  sueloAzulList[i][2] == 0: # esta desactivado --> lo pasamos a activo

                    spawnx, spawny = sueloAzulList[i][3], sueloAzulList[i][4]
                    
                    cambioAzulNormal, cambioAzulNormal_rect , posicionXBloque, posicionYBloque= sueloNormal(spawnx,spawny,0,0,1) # 1 de azul
                    sueloAzulList[i] = (cambioAzulNormal,cambioAzulNormal_rect, 1, posicionXBloque, posicionYBloque)
            
            #BLOQUES ROJOS
            for i in range (numBlocsRojosTotal):

                if sueloRojoList[i][2] == 1: # esta activo --> lo pasamos a raya
                
                    spawnx, spawny = sueloRojoList[i][3], sueloRojoList[i][4]

                    cambioAzulRaya, cambioAzulRaya_rect, posicionXBloque, posicionYBloque = sueloRaya(spawnx,spawny,0,0,2) # 1 de azul
                    sueloRojoList[i] = (cambioAzulRaya,cambioAzulRaya_rect, 0, posicionXBloque, posicionYBloque)

                elif  sueloRojoList[i][2] == 0: # esta desactivado --> lo pasamos a activo

                    spawnx, spawny = sueloRojoList[i][3], sueloRojoList[i][4]
                    
                    cambioRojoNormal, cambioRojoNormal_rect , posicionXBloque, posicionYBloque= sueloNormal(spawnx,spawny,0,0,2) # 1 de azul
                    sueloRojoList[i] = (cambioRojoNormal,cambioRojoNormal_rect, 1, posicionXBloque, posicionYBloque)
            
            #PINCHOS AZULES
            for i in range(numPinchosAzulesTotal):

                if sueloPinchoAzulList[i][2] == 1: # esta activo --> lo pasamos a raya
                
                    spawnx, spawny, rotacion  = sueloPinchoAzulList[i][3], sueloPinchoAzulList[i][4],  sueloPinchoAzulList[i][5]

                    cambioAzulRaya, cambioAzulRaya_rect, posicionXBloque, posicionYBloque, rotacion = Pinchos(spawnx,spawny,0,0,0,rotacion) # 0 pincho azul raya
                    sueloPinchoAzulList[i] = (cambioAzulRaya,cambioAzulRaya_rect, 0, posicionXBloque, posicionYBloque, rotacion)

                elif  sueloPinchoAzulList[i][2] == 0: # esta desactivado --> lo pasamos a activo

                    spawnx, spawny, rotacion = sueloPinchoAzulList[i][3], sueloPinchoAzulList[i][4], sueloPinchoAzulList[i][5]
                    
                    cambioRojoNormal, cambioRojoNormal_rect , posicionXBloque, posicionYBloque, rotacion= Pinchos(spawnx,spawny,0,0,2, rotacion) # 2 pincho azul normal
                    sueloPinchoAzulList[i] = (cambioRojoNormal,cambioRojoNormal_rect, 1, posicionXBloque, posicionYBloque, rotacion)

            #PINCHOS ROJOS
            for i in range(numPinchosRojosTotal):

                if sueloPinchoRojoList[i][2] == 1: # esta activo --> lo pasamos a raya
                
                    spawnx, spawny , rotacion = sueloPinchoRojoList[i][3], sueloPinchoRojoList[i][4], sueloPinchoAzulList[i][5]

                    cambioAzulRaya, cambioAzulRaya_rect, posicionXBloque, posicionYBloque, rotacion = Pinchos(spawnx,spawny,0,0,1, rotacion) # 1 pincho rosa raya
                    sueloPinchoRojoList[i] = (cambioAzulRaya,cambioAzulRaya_rect, 0, posicionXBloque, posicionYBloque, rotacion)

                elif sueloPinchoRojoList[i][2] == 0: # esta desactivado --> lo pasamos a activo

                    spawnx, spawny , rotacion = sueloPinchoRojoList[i][3], sueloPinchoRojoList[i][4], sueloPinchoAzulList[i][5]
                    
                    cambioRojoNormal, cambioRojoNormal_rect , posicionXBloque, posicionYBloque, rotacion= Pinchos(spawnx,spawny,0,0,3, rotacion) # 3 pincho rosa normal
                    sueloPinchoRojoList[i] = (cambioRojoNormal,cambioRojoNormal_rect, 1, posicionXBloque, posicionYBloque, rotacion)





















        # MOVIMIENTO DEL PINGUINO


        # Obtener el estado del teclado
        velocidadx = 1
        velocidady = 2

        # Actualizar la posición del pinguino según las teclas presionadas
        if teclas[pygame.K_LEFT]:
            if porque_si:
                if direccion_derecha:  # Cambiar de dirección solo si es necesario
                    pinguino = pygame.transform.flip(pinguino, True, False)
                    direccion_derecha = False
                pinguino_rect.x -= velocidadx
            
        if teclas[pygame.K_RIGHT]:
            if porque_si:
                if not direccion_derecha:  # Cambiar de dirección solo si es necesario
                    pinguino = pygame.transform.flip(pinguino, True, False)
                    direccion_derecha = True
                pinguino_rect.x += velocidadx

        if teclas[pygame.K_DOWN]:
            pinguino_rect.y += velocidady































        # COLISION ENTRE OBJETOS



        # PINGUINO CON RECTANGULO
        if pinguino_rect.colliderect(rectangulo_rect):
            print("¡Colisión!")
            rip = True
            rectangulo_rect.x = -100000
            rectangulo_rect.y = -100000
            return 3
        

        # PINGUINO CON BLOQUES Verdes
        for i in range(numBlocsVerds):
            if pinguino_rect.colliderect(sueloVerdeList[i][1]):
                #print("¡Colisión 2!")
                #pinguino_rect.y = velocidad_y
                pinguino_rect.y = sueloVerdeList[i][1].y - pinguino_rect.height
                en_suelo = True











        
        
        # PINGUINO CON BLOQUES AZULES
                

        for i in range(numBlocsAzulesTotal):

            #print(pinguino_rect.y,sueloAzulList[i][1].y + sueloAzulList[i][1].height) #LAG GENERATOR

            if sueloAzulList[i][2] == 1:

                # CABEZA PINGUINO CON TECHO
                condicion1 = pinguino_rect.y == sueloAzulList[i][1].y + sueloAzulList[i][1].height #que la cabeza del pinguino toca la parte de abajo
                condicion2 =  sueloAzulList[i][1].x <= pinguino_rect.x <= sueloAzulList[i][1].x + sueloAzulList[i][1].width # que la esquina izquierda esta dentro del rango del bloque
                condicion3 = sueloAzulList[i][1].x <= pinguino_rect.x + pinguino_rect.width <= sueloAzulList[i][1].x + sueloAzulList[i][1].width # que la esquina derecha esta dentro del rango del blqoue
                #if  condicion1 and condicion2 and condicion3 :

                if condicion1 and condicion3: # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                    salto_en_curso = False # detenemos salto
                    velocidad_y = 0

                # DERECHA PINGUINO CON IZQUIERDA DEL BLOQUE
                    
                condicion1 = pinguino_rect.x + pinguino_rect.width == sueloAzulList[i][1].x
                condicion3 = sueloAzulList[i][1].y <= pinguino_rect.y + pinguino_rect.height / 2 <= sueloAzulList[i][1].y + sueloAzulList[i][1].height

                if condicion1 and condicion3:
                    print("boom")
                    pinguino_rect.x = 1700
                    boom = True


                # PIE PINGUINO CON SUELO
                condicion1 = pinguino_rect.y + pinguino_rect.height  == sueloAzulList[i][1].y  #que la cabeza del pinguino toca la parte de abajo
                condicion3 = sueloAzulList[i][1].x <= pinguino_rect.x + pinguino_rect.width <= sueloAzulList[i][1].x + sueloAzulList[i][1].width # que la esquina derecha esta dentro del rango del blqoue

                SuperPosicion = pinguino_rect.colliderect(sueloAzulList[i][1].inflate(-5, -5))

                #if (condicion1 and condicion3) : # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                if pinguino_rect.colliderect(sueloAzulList[i][1]): # no se pero funciona fuck it
                    #salto_en_curso = False # detenemos salto
                    en_suelo = True # estamos en el foking suelo
                    pinguino_rect.y = sueloAzulList[i][1].y - pinguino_rect.height   # no lo movemos
                    #print("Condicion de tocar hierba")
                    #velocidad_y = 0               

                # INTERIOR CON OTRO INTERIOR

                #if condicion1 and condicion3: # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                if SuperPosicion : # no se pero funciona fuck it
                    pinguino_rect.x = 1700
                    print("BUUUUUUUUUUUUM")
                    boom = True

        













        # PINGUINO CON BLOQUES ROJOS
                    
        for i in range(numBlocsRojosTotal):

            #print(pinguino_rect.y,sueloAzulList[i][1].y + sueloAzulList[i][1].height) LAG GENERATOR

            if sueloRojoList[i][2] == 1:

                # CABEZA PINGUINO CON TECHO
                condicion1 = pinguino_rect.y == sueloRojoList[i][1].y + sueloRojoList[i][1].height #que la cabeza del pinguino toca la parte de abajo
                condicion2 =  sueloRojoList[i][1].x <= pinguino_rect.x <= sueloRojoList[i][1].x + sueloRojoList[i][1].width # que la esquina izquierda esta dentro del rango del bloque
                condicion3 = sueloRojoList[i][1].x <= pinguino_rect.x + pinguino_rect.width <= sueloRojoList[i][1].x + sueloRojoList[i][1].width # que la esquina derecha esta dentro del rango del blqoue
                #if  condicion1 and condicion2 and condicion3 :

                if condicion1 and condicion3: # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                    salto_en_curso = False # detenemos salto
                    velocidad_y = 0

                # DERECHA PINGUINO CON IZQUIERDA DEL BLOQUE
                    
                condicion1 = pinguino_rect.x + pinguino_rect.width == sueloRojoList[i][1].x
                condicion3 = sueloRojoList[i][1].y <= pinguino_rect.y + pinguino_rect.height / 2 <= sueloRojoList[i][1].y + sueloRojoList[i][1].height

                if condicion1 and condicion3:
                    print("boom")
                    pinguino_rect.x = 700
                    boom = True

                # PIE PINGUINO CON SUELO
                condicion1 = pinguino_rect.y + pinguino_rect.height  == sueloRojoList[i][1].y  #que la cabeza del pinguino toca la parte de abajo
                condicion3 = sueloRojoList[i][1].x <= pinguino_rect.x + pinguino_rect.width <= sueloRojoList[i][1].x + sueloRojoList[i][1].width # que la esquina derecha esta dentro del rango del blqoue

                SuperPosicion = pinguino_rect.colliderect(sueloRojoList[i][1].inflate(-5, -5))

                #if (condicion1 and condicion3) : # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                if pinguino_rect.colliderect(sueloRojoList[i][1]): # no se pero funciona fuck it
                    #salto_en_curso = False # detenemos salto
                    en_suelo = True # estamos en el foking suelo
                    pinguino_rect.y = sueloRojoList[i][1].y - pinguino_rect.height   # no lo movemos
                    #print("Condicion de tocar hierba")
                    #velocidad_y = 0               

                # INTERIOR CON OTRO INTERIOR

                #if condicion1 and condicion3: # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                if SuperPosicion : # no se pero funciona fuck it
                    pinguino_rect.x = 1700
                    print("BUUUUUUUUUUUUM")
                    boom = True
        

        #PINGUINO CON PINCHOS
                    
        for i in range(numPinchosRojosTotal):
            
            if sueloPinchoRojoList[i][2] == 1:

                SuperPosicion = pinguino_rect.colliderect(sueloPinchoRojoList[i][1].inflate(-10, -10))

                if SuperPosicion:
                    boom = True
                    pinguino_rect.x = 10000
        
        for i in range(numPinchosAzulesTotal):
            
            if sueloPinchoAzulList[i][2] == 1:

                SuperPosicion = pinguino_rect.colliderect(sueloPinchoAzulList[i][1].inflate(-10, -10))

                if SuperPosicion:
                    boom = True
                    pinguino_rect.x = 10000

        
        # SALIR
        
        if pinguino_rect.colliderect( sexoInfo[1].inflate(-50,-50)  ):
            return 0 # da igual, sera modo especial
        
        if pinguino_rect.colliderect( salirInfo[1].inflate(-50,-50)  ):
            return 1 # salir 

        if pinguino_rect.colliderect( empezarInfo[1].inflate(-50,-50)  ):
            return 3 # modo normal

























        # COLISION TECHO Y SUELO


        # SUELO PANTALLA
        if pinguino_rect.y >= height - pinguino_rect.height:
            pinguino_rect.y = height - pinguino_rect.height
            en_suelo = True

        # TECHO PANTALLA
        if pinguino_rect.y <= 0:
            pinguino_rect.y = 0
            velocidad_y = 0  # Detener el movimiento hacia arriba cuando toca el techo





























        # FONDO + OBJETOS

        #cambiar el tamaño de forma dinamica (tiembla la pantalla!!)
        a = 0
        b = 0
        #window = pygame.display.set_mode((width + a, height + b))



        #usar la imagen de fondo
        window.blit(fondo, (0, 0))
        window.blit(text_surface, (scorex,scorey))

        # IMAGEN PANTALLA
        #window.fill((250, 0, 250))  # Rellenar la pantalla de morado

        #imprimir objetos
        if rip: # no quiero un rectangulo
            pygame.draw.rect(window, rectangulo_color, rectangulo_rect)
        window.blit(pinguino, pinguino_rect)
        for i in range(numBlocsVerds):
            window.blit(sueloVerdeList[i][0], sueloVerdeList[i][1])
        for i in range( numBlocsAzulesTotal ):
            window.blit(sueloAzulList[i][0], sueloAzulList[i][1])
        for i in range( numBlocsRojosTotal ):
            window.blit(sueloRojoList[i][0], sueloRojoList[i][1])

        for i in range( numPinchosAzulesTotal ):
            window.blit(sueloPinchoAzulList[i][0], sueloPinchoAzulList[i][1])
        for i in range( numPinchosRojosTotal ):
            window.blit(sueloPinchoRojoList[i][0], sueloPinchoRojoList[i][1])
        
        window.blit( salirInfo[0], salirInfo[1]  )
        window.blit( sexoInfo[0], sexoInfo[1]  )
        window.blit( empezarInfo[0], empezarInfo[1]  )

        # Dibujar el pingüino encima del fondo
        window.blit(pinguino, pinguino_rect)


        # Actualizar la pantalla
        pygame.display.flip()
        

        #pygame.time.delay(500)

    pygame.quit()



def xd():

    # Configuración de la ventana
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mi Primer Juego")

    fondo = pygame.image.load(r"fotosPython\xd.jpg")
    
    pygame.display.set_caption("vaya noob")

    # Inicializar el mezclador de audio
    pygame.mixer.init()


    # Cargar un archivo de audio en formato OGG
    sonido_ogg = pygame.mixer.Sound(r"fotosPython\JAJAJAJA.ogg")
    volumen = 0.2  # Valor entre 0.0 (silencio) y 1.0 (volumen máximo)
    sonido_ogg.set_volume(volumen)

    tiempo_inicial = pygame.time.get_ticks()
    hasonado = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not hasonado:
            sonido_ogg.play()
            hasonado = True

        tiempo_actual = pygame.time.get_ticks()

        # Reproducir el sonido después de 5 segundos (5000 milisegundos)
        if tiempo_actual - tiempo_inicial >= 4400:
            running = False

        window.blit(fondo, (0, 0))
        pygame.display.flip()


# WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW































# --------------------------- NIVELES -----------------------------------------






















# WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW






"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠐⠒⠒⠲⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠴⠛⠁⠀⢈⠀⢒⣀⡤⠤⠄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠑⠚⠀⠀⠁⠀⠒⢉⣤⠤⠒⠒⠒⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡞⢡⢦⠀⠀⠀⠀⠀⠀⠚⠁⣀⡤⠔⠒⠒⠒⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡏⣠⠾⠈⠀⠀⠀⠀⠀⠀⠀⠀⢁⣠⠤⢖⠒⠒⠛⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠈⢧⣀⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⡤⣶⣮⣿⡽⣶⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡤⠖⠊⠹⣿⣽⡗⠚⠻⠷⣒⢶⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠛⠳⠤⢤⣤⡤⠤⠴⣦⠀⠀⠳⣄⣀⠀⣙⡿⢣⠀⠀⠀⠈⠻⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⢻⠛⠒⠀⠀⠉⠉⠁⢀⣸⡇⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠚⠃⠒⠒⠒⠒⠉⠉⣁⣀⣷⡀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠒⠒⠚⢻⡉⠉⢹⡄⠘⢷⡀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⢧⠀⠈⠛⠒⠒⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡄⠘⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠻⣄⢳⡙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠣⡀⠘⣿⣿⠛⡟⠲⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣖⠋⠀⠀⠀⡈⠛⠃⠙⠀⢳⡀⠀⠙⣶⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡰⠟⠉⣷⣄⣠⣾⠁⠀⠀⠀⠀⠸⡗⠦⢴⣁⠉⠳⢤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⣠⠎⠛⠛⠁⡇⠀⠀⠀⠀⠀⠀⢻⠀⠀⠈⠳⣄⠀⠈⣷
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠐⢦⣞⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⢀⡜⠁⠀⢰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠈⠙⠲⠤⣀⣠⡇⠀⠀⠀⠀⠀⠀⠀⢹⣠⠞⠀⠀⢠⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢄⡀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠈⡏⠀⠀⢠⣷⣒⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣓⣦⡀⠀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⢳⠀⠀⣯⣭⢁⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⠹⣷⣾⣿⡄⠀⠀⢀⣿⣤⣤⣤⣤⠴⠚⣏⠀⠀⠸⣠⠎⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⣈⠉⠁⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⡏⠉⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠹⢦⡀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⢰⠖⢻⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡞⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⢸⠀⠀⠀⠀⠀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠙⡆⠀⠀⠀⣸⠀⠀⡇⢸⡀⠀⠀⠀⡶⠏⠉⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⡺⢦⣸⣀⣠⢴⠇⠀⠀⡇⠘⣧⠤⠤⢼⡣⢦⣤⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢹⣏⡇⠀⠻⡗⠶⠋⠀⠀⢰⡇⠀⢻⣀⣠⠏⠀⣞⣮⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣤⠀⡀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠊⠁⡼⠀⠀⠓⣃⣸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣛⠺⢭⣽⣦⠤⠤⠤⠒⠒⠉⠉⠉⠒⠤⠤⣄⣠⣯⣷⣿⣟⠀
"""


























































































































































































































































"""


"""









"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡤⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠀⡀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠘⡆⡜⠁⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⣀⣤⡂⠀⠇⠱⠀⡀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⡀⢠⣟⢭⣥⣤⠽⡆⠀⡶⣊⣉⣲⣤⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⡀⠀⠐⠂⠘⠄⣈⣙⡡⡴⠀⠀⠙⣄⠙⣛⠜⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠄⠊⠀⠀⠀⠀⡸⠛⠀⠀⠀⢸⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⢄⣘⣄⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⣇⡀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠈⡟⠒⠲⣄⠀⠀⡰⠇⠖⢄⠀⠀⡹⡇⢀⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⡇⠀⠀⠹⠀⡞⠀⠀⢀⠤⣍⠭⡀⢱⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⠞⠀⠀⢠⡇⠀⠀⠀⠀⠁⠀⢴⠥⠤⠦⠦⡼⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣤⣴⣶⣿⣿⡟⠁⠀⠋⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠑⣠⢤⠐⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠬⠥⣄⠀⠀⠈⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⢀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠦⠤⢤⣄⣀⣠⠤⢿⣶⣶⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀






⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿











"""
























def generador(longitud):

    #La x y la distancia no dependera de la parte sino del bucle

    #Saber tipo de bloque y poner bien en ambas listas ! (azules y rosa raya en lista normal, lo otro en inversa)
    #numero de bloques
    #La y

    # Tipo de bloque
    # la x
    # la y 
    # Altura
    # Numero de bloques
    # Estado (1 o 0) o None (verde)
    # Rotacion
    # Fliping

    # Poner en fila
    # Poner en columna (no suma distancia, poner 2 columnas implica sumar la x con la distancia entre estos)


    
                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner1 = [ ("BloqueVerde" , 50   ,600   ,35  ,None   ,90        ,None         , "Fila"    ,       0      ),
                
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       8      ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       11     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       15     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       18     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       21     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       24     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       27     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       30     ) ]
    

    """
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
    ...............................................

    """
                #tipo             x     y     num   estado rotacion  fliping/no suma  fila o columna   distancia a restar
    Spawner2 = [ ("BloqueVerde"  , 50  ,600   ,30  ,None   ,90         ,None         , "Fila"    ,       0      ),
                
                ("BloqueAzul"   , 50  ,400    ,8   ,1      ,90         ,"no"         , "Fila"    ,       23     ),
                ("PinchoVerde"  , 50  ,350    ,8   ,1      ,270        ,"no"         , "Fila"    ,       23     ),
                ("PinchoAzul"   , 50  ,550    ,8   ,1      ,270        ,"no"         , "Fila"    ,       23     ),  #30 de posicion + 8 anteriores
                ("PinchoAzul"   , 50  ,550    ,8   ,1      ,270        ,"no"         , "Fila"    ,       10     ),
                ("BloqueRosa"   , 50  ,400    ,8   ,0      ,90         ,"no"         , "Fila"    ,       10     ),
                ("PinchoRosa"   , 50  ,350    ,8   ,0      ,270        ,"no"         , "Fila"    ,       10     ) ]
    

    """
            
                                        Δ Δ Δ Δ Δ Δ 
            ❐❐❐❐❐❐❐❐❐❐❐❐        ❐❐❐❐❐❐❐❐            ???
            Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ         Δ Δ Δ Δ Δ Δ 
    ................................................................

    """
                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner3 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,4   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 350    ,4   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       9     ),
                ("BloqueAzul"   , 50  , 350    ,4   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
            ❐         ❑      
            ❐       Δ ❑      
            ❐       Δ ❑      
            ❐       Δ ❑      
    ...............................................
    """

                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner4 = [ ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90        ,None         , "Fila"    ,        0      ),
                ("BloqueAzul"   , 50  , 600    ,7   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,7   ,0      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueAzul"   , 50  , 600    ,7   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,7   ,0      ,90         ,None         , "Fila"    ,        0     ),

                ("BloqueAzul"   , 50  , 452    ,7   ,1      ,90         ,"no"       , "Fila"    ,          28     ),
                ("BloqueRosa"   , 50  , 452    ,7   ,0      ,90         ,"no"         , "Fila"    ,        21     ),
                ("BloqueAzul"   , 50  , 402    ,7   ,1      ,90         ,"no"         , "Fila"    ,        14     ),
                ("BloqueRosa"   , 50  , 402    ,7   ,0      ,90         ,"no"         , "Fila"    ,        7     ),

                ("PinchoVerde"   , 50  , 780    ,28   ,0      ,270         ,"no"         , "Fila"    ,       28     ),
    
            
                ("PinchoRosa"   , 50  , 402    ,7   ,0      ,270         ,"no"         , "Fila"    ,      21     ),
                ("PinchoAzul"   , 50  , 402    ,7   ,1      ,270         ,"no"         , "Fila"    ,      28     ),
                ("PinchoRosa"   , 50  , 450    ,7   ,0      ,90         ,"no"         , "Fila"    ,       14     ),
                ("PinchoAzul"   , 50  , 450    ,7   ,1      ,90         ,"no"         , "Fila"    ,       7     ),

                ("BloqueVerde"  , 50  , 600    ,5  ,None   ,90         ,None         , "Fila"    ,       0      ) ]
                

    """
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ❑❑❑❑❑❑❐❐❐❐❐
                ❑❑❑❑❑❑❐❐❐❐❐ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ


    ............❑❑❑❑❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """


                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner5 = [ 
                ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90         ,None         , "Fila"       ,         0      ),
                ("BloqueAzul"   , 50  , 600    ,10  ,1      ,270       ,None         , "Columna"      ,        -1     ),
                ("PinchoVerde"  , 50  , 780    ,50  ,1      ,270           ,None         , "Fila"    ,        0      ),

                ("BloqueAzul"   , 50  , 403    ,1   ,1      ,90         ,None         , "Columna"    ,        45     ),
                ("BloqueAzul"   , 50  , 203    ,1   ,1      ,90         ,None         , "Columna"    ,        45     ), 
                ("PinchoAzul"   , 50  , 153    ,1   ,1      ,270        ,None         , "Columna"    ,        45     ),#Parte 1

                ("BloqueAzul"   , 50  , 700    ,1   ,1      ,90         ,None         , "Columna"    ,        41     ), 
                ("BloqueAzul"   , 50  , 400    ,1   ,1      ,90         ,None         , "Columna"    ,        41     ),
                ("PinchoAzul"   , 50  , 350    ,1   ,1      ,270        ,None         , "Columna"    ,        41     ),#Parte 2


                ("BloqueRosa"   , 50  , 400    ,1   ,0      ,90         ,None         , "Columna"    ,        35     ),
                ("BloqueRosa"   , 50  , 200    ,1   ,0      ,90         ,None         , "Columna"    ,        35     ), #Parte 1
                ("PinchoRosa"   , 50  , 150    ,1   ,0      ,270         ,None         , "Columna"    ,       35     ),

                ("BloqueRosa"   , 50  , 600    ,10   ,0      ,180       ,None         , "Columna"    ,        32     ),  # COLUMNA


                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        31     ), #Parte 2
                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        30     ),
                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        29     ),
                ("BloqueRosa"   , 50  , 402    ,1   ,0      ,90         ,None         , "Columna"    ,        30     ),
                ("PinchoRosa"   , 50  , 352    ,1   ,0      ,270        ,None         , "Columna"    ,        30     ),


                ("BloqueVerde"  , 50  , 600    ,15  ,None   ,90         ,"no"         , "Fila"    ,           25      ), ]
                
    

    """
                  Δ     Δ    Δ      Δ 
                  ❑    ❑    ❑     ❑


    ............  ❑    ❑    ❑     ❑          ❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """


    PRUEBAS = [ ("BloqueVerde"  , 50  ,600    ,30  ,None   ,90         ,None         , "Fila"    ,       0      ),
                ("BloqueAzul"   , 50  ,300    ,8   ,1      ,90         ,None         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  ,300    ,8   ,0      ,270        ,None         , "Fila"    ,       30     ),
                ("BloqueAzul"   , 50  ,300    ,8   ,0      ,90         ,None         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  ,300    ,8   ,1      ,270        ,None         , "Fila"    ,       30     )]
    
    # notas de creacion :
        # la y cuidado porque el salto puede moverse 2 pixeles y hacer bypass de la colision :(



    S1 = Spawner1
    S2 = Spawner2
    S3 = Spawner3
    S4 = Spawner4
    S5 = Spawner5

    S = [S1,S2,S3,S4,S5]
    Spawner = []

    for i in range(longitud):
        randomNumber = random.randint(0,4)
        Spawner += S[randomNumber]

    #Spawner = S1  



    



    # Variables

    distancia = 0 # ir sumando el numero de bloques adjacentes 
    Puestos = 0

    sueloVerdeList = []

    sueloAzulList = []
    sueloAzulInversoList = []

    sueloRojoList = []
    sueloRojoInversoList = []

    # 0 verde, 1 azul, 2 Rojo
    suelo = [ (sueloVerdeList,None) , (sueloAzulList, sueloAzulInversoList ) , (sueloRojoList, sueloRojoInversoList)   ]

    contador = 0

    while contador != len(Spawner):

        Tipo =   Spawner[contador][0]
        spawnx = Spawner[contador][1]
        spawny = Spawner[contador][2]
        Nspawn = Spawner[contador][3]
        BlocState = Spawner[contador][4]
        Rotar = Spawner[contador][5]
        Flip = Spawner[contador][6]

        Colocacion = Spawner[contador][7]
        DistanciaArestar = Spawner[contador][8]

        contador += 1
        index = -1

        #Seleccionar la lista a añadir
        if Tipo == "BloqueVerde" or Tipo == "PinchoVerde" :
            index = 0
            normalOnly = True 

        elif Tipo == "BloqueAzul" or Tipo == "PinchoAzul":
            index = 1
            normalOnly = False
        
        elif Tipo == "BloqueRosa" or Tipo == "PinchoRosa":
            index = 2
            normalOnly = False
        
        nosuma = False
        if Flip == "no":
            nosuma = True
            Flip = None

        if index == -1:
            return NameError
        


        if Colocacion == "Fila":

            for i in range(Nspawn):

                Info = Bloques(spawnx , spawny , i + distancia - DistanciaArestar , 0 , Tipo , BlocState , Rotar , Flip ) 
                suelo[index][0].append((Info[0],Info[1],Info[2],Info[3],Info[4]))

                if not normalOnly:
                    
                    Info = Bloques(spawnx , spawny , i + distancia - DistanciaArestar , 0 , Tipo , int(not BlocState) , Rotar , Flip ) 
                    suelo[index][1].append((Info[0],Info[1],Info[2],Info[3],Info[4]))
            
            if not nosuma :

                distancia += Nspawn
        
        elif Colocacion == "Columna":

            for i in range(Nspawn):

                Info = Bloques(spawnx , spawny , distancia - DistanciaArestar , -i , Tipo , BlocState , Rotar , Flip ) 
                suelo[index][0].append((Info[0],Info[1],Info[2],Info[3],Info[4]))

                if not normalOnly:
                    
                    Info = Bloques(spawnx , spawny , distancia - DistanciaArestar, -i , Tipo , int(not BlocState) , Rotar , Flip ) 
                    suelo[index][1].append((Info[0],Info[1],Info[2],Info[3],Info[4]))
        

            
        
        Puestos += Nspawn


    return suelo , Puestos




#Levels con velocidad 2
def Levels():
    #La x y la distancia no dependera de la parte sino del bucle

    #Saber tipo de bloque y poner bien en ambas listas ! (azules y rosa raya en lista normal, lo otro en inversa)
    #numero de bloques
    #La y

    # Tipo de bloque
    # la x
    # la y 
    # Altura
    # Numero de bloques
    # Estado (1 o 0) o None (verde)
    # Rotacion
    # Fliping

    # Poner en fila
    # Poner en columna (no suma distancia, poner 2 columnas implica sumar la x con la distancia entre estos)


    
                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner1 = [ ("BloqueVerde" , 50   ,600   ,35  ,None   ,90        ,None         , "Fila"    ,       0      ),
                
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       8      ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       11     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       15     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       18     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       21     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       24     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       27     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       30     ) ]
    

    """
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
    ...............................................

    """
                #tipo             x     y     num   estado rotacion  fliping/no suma  fila o columna   distancia a restar
    Spawner2 = [ ("BloqueVerde"  , 50  ,600   ,30  ,None   ,90         ,None         , "Fila"    ,       0      ),
                
                ("BloqueAzul"   , 50  ,400    ,8   ,1      ,90         ,"no"         , "Fila"    ,       23     ),
                ("PinchoVerde"  , 50  ,350    ,8   ,1      ,270        ,"no"         , "Fila"    ,       23     ),
                ("PinchoAzul"   , 50  ,550    ,8   ,1      ,270        ,"no"         , "Fila"    ,       23     ),  #30 de posicion + 8 anteriores
                ("PinchoAzul"   , 50  ,550    ,8   ,1      ,270        ,"no"         , "Fila"    ,       10     ),
                ("BloqueRosa"   , 50  ,400    ,8   ,0      ,90         ,"no"         , "Fila"    ,       10     ),
                ("PinchoRosa"   , 50  ,350    ,8   ,0      ,270        ,"no"         , "Fila"    ,       10     ) ]
    

    """
            
                                        Δ Δ Δ Δ Δ Δ 
            ❐❐❐❐❐❐❐❐❐❐❐❐        ❐❐❐❐❐❐❐❐            ???
            Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ         Δ Δ Δ Δ Δ Δ 
    ................................................................

    """
                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner3 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,4   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 350    ,4   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       9     ),
                ("BloqueAzul"   , 50  , 350    ,4   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
            ❐         ❑      
            ❐       Δ ❑      
            ❐       Δ ❑      
            ❐       Δ ❑      
    ...............................................
    """

                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner4 = [ ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90        ,None         , "Fila"    ,        0      ),
                ("BloqueAzul"   , 50  , 600    ,7   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,7   ,0      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueAzul"   , 50  , 600    ,7   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,7   ,0      ,90         ,None         , "Fila"    ,        0     ),

                ("BloqueAzul"   , 50  , 452    ,7   ,1      ,90         ,"no"       , "Fila"    ,          28     ),
                ("BloqueRosa"   , 50  , 452    ,7   ,0      ,90         ,"no"         , "Fila"    ,        21     ),
                ("BloqueAzul"   , 50  , 402    ,7   ,1      ,90         ,"no"         , "Fila"    ,        14     ),
                ("BloqueRosa"   , 50  , 402    ,7   ,0      ,90         ,"no"         , "Fila"    ,        7     ),

                ("PinchoVerde"   , 50  , 780    ,28   ,0      ,270         ,"no"         , "Fila"    ,       28     ),
    
            
                ("PinchoRosa"   , 50  , 402    ,7   ,0      ,270         ,"no"         , "Fila"    ,      21     ),
                ("PinchoAzul"   , 50  , 402    ,7   ,1      ,270         ,"no"         , "Fila"    ,      28     ),
                ("PinchoRosa"   , 50  , 450    ,7   ,0      ,90         ,"no"         , "Fila"    ,       14     ),
                ("PinchoAzul"   , 50  , 450    ,7   ,1      ,90         ,"no"         , "Fila"    ,       7     ),

                ("BloqueVerde"  , 50  , 600    ,5  ,None   ,90         ,None         , "Fila"    ,       0      ) ]
                

    """
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ❑❑❑❑❑❑❐❐❐❐❐
                ❑❑❑❑❑❑❐❐❐❐❐ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ


    ............❑❑❑❑❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """


                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner5 = [ 
                ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90         ,None         , "Fila"       ,         0      ),
                ("BloqueAzul"   , 50  , 600    ,10  ,1      ,270       ,None         , "Columna"      ,        -1     ),
                ("PinchoVerde"  , 50  , 780    ,50  ,1      ,270           ,None         , "Fila"    ,        0      ),

                ("BloqueAzul"   , 50  , 403    ,1   ,1      ,90         ,None         , "Columna"    ,        45     ),
                ("BloqueAzul"   , 50  , 203    ,1   ,1      ,90         ,None         , "Columna"    ,        45     ), 
                ("PinchoAzul"   , 50  , 153    ,1   ,1      ,270        ,None         , "Columna"    ,        45     ),#Parte 1

                ("BloqueAzul"   , 50  , 700    ,1   ,1      ,90         ,None         , "Columna"    ,        41     ), 
                ("BloqueAzul"   , 50  , 400    ,1   ,1      ,90         ,None         , "Columna"    ,        41     ),
                ("PinchoAzul"   , 50  , 350    ,1   ,1      ,270        ,None         , "Columna"    ,        41     ),#Parte 2


                ("BloqueRosa"   , 50  , 400    ,1   ,0      ,90         ,None         , "Columna"    ,        35     ),
                ("BloqueRosa"   , 50  , 200    ,1   ,0      ,90         ,None         , "Columna"    ,        35     ), #Parte 1
                ("PinchoRosa"   , 50  , 150    ,1   ,0      ,270         ,None         , "Columna"    ,       35     ),

                ("BloqueRosa"   , 50  , 600    ,10   ,0      ,180       ,None         , "Columna"    ,        32     ),  # COLUMNA


                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        31     ), #Parte 2
                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        30     ),
                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        29     ),
                ("BloqueRosa"   , 50  , 402    ,1   ,0      ,90         ,None         , "Columna"    ,        30     ),
                ("PinchoRosa"   , 50  , 352    ,1   ,0      ,270        ,None         , "Columna"    ,        30     ),


                ("BloqueVerde"  , 50  , 600    ,15  ,None   ,90         ,"no"         , "Fila"    ,           25      ), ]
                
    

    """
                  Δ     Δ    Δ      Δ 
                  ❑    ❑    ❑     ❑


    ............  ❑    ❑    ❑     ❑          ❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """


    PRUEBAS = [ ("BloqueVerde"  , 50  ,600    ,30  ,None   ,90         ,None         , "Fila"    ,       0      ),
                ("BloqueAzul"   , 50  ,300    ,8   ,1      ,90         ,None         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  ,300    ,8   ,0      ,270        ,None         , "Fila"    ,       30     ),
                ("BloqueAzul"   , 50  ,300    ,8   ,0      ,90         ,None         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  ,300    ,8   ,1      ,270        ,None         , "Fila"    ,       30     )]
    
    # notas de creacion :
        # la y cuidado porque el salto puede moverse 2 pixeles y hacer bypass de la colision :(



    S1 = Spawner1
    S2 = Spawner2
    S3 = Spawner3
    S4 = Spawner4
    S5 = Spawner5

    S = [S1,S2,S3,S4,S5]


    return S


#Velocidad Bloque 4
def LevelsHardcore():
    #La x y la distancia no dependera de la parte sino del bucle

    #Saber tipo de bloque y poner bien en ambas listas ! (azules y rosa raya en lista normal, lo otro en inversa)
    #numero de bloques
    #La y

    # Tipo de bloque
    # la x
    # la y 
    # Altura
    # Numero de bloques
    # Estado (1 o 0) o None (verde)
    # Rotacion
    # Fliping

    # Poner en fila
    # Poner en columna (no suma distancia, poner 2 columnas implica sumar la x con la distancia entre estos)


    
                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner1 = [ ("BloqueVerde" , 50   ,600   ,35  ,None   ,90        ,None         , "Fila"    ,       0      ),
                
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       8      ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       11     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       15     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       18     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       21     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       24     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       27     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       30     ) ]
    

    """
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
    ...............................................

    """
    # Descripcion 1 : bloques mu juntos :()


    Spawner101 = [ ("BloqueVerde" , 50   ,600   ,40  ,None   ,90        ,None         , "Fila"    ,       0      ),
                
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,        5      ),
                ("PinchoVerde"   , 50  ,550   ,1   ,1      ,270         ,None         , "Columna" ,       8      ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       11     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       15     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       19     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       23     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       27     ), 
                ("BloqueAzul"   , 50  ,550    ,8   ,1      ,0         ,None         , "Columna" ,       31     ),
                ("BloqueRosa"   , 50  ,550    ,8   ,0      ,0         ,None         , "Columna" ,       35     ) ]
    

    """
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐      ❑
            ❐      ❑      ❐  Δ   ❑
    ...............................................

    """

    # Descripcion 101 : Ahora tiene un pinchito :D   


                #tipo             x     y     num   estado rotacion  fliping/no suma  fila o columna   distancia a restar
    Spawner2 = [ ("BloqueVerde"  , 50  ,600   ,30  ,None   ,90         ,None         , "Fila"    ,       0      ),

                ("PinchoAzul"   , 50  ,550    ,5   ,1      ,270         ,"no"         , "Fila"    ,       5     ),     
                ("PinchoRosa"   , 50  ,550    ,5   ,0      ,270        ,"no"          , "Fila"    ,       10     ),
                 ("PinchoAzul"   , 50  ,550    ,5   ,1      ,270         ,"no"         , "Fila"    ,      15     ),     
                ("PinchoRosa"   , 50  ,550    ,5   ,0      ,270        ,"no"          , "Fila"    ,       20     ) ]
    

    """
            
            Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ 
    ................................................................

    """

    # Descripcion 2 : mas pinchos?



                #tipo             x     y     num   estado rotacion  fliping/no suma  fila o columna   distancia a restar
    Spawner201 = [ 
        
                ("BloqueVerde"  , 50  ,600   ,10  ,None   ,90         ,"no"         , "Fila"    ,       0      ),
                ("BloqueVerde"  , 50  ,600   ,40  ,None   ,90         ,"si"         , "Fila"    ,       0      ),


                ("BloqueRosa"   , 50  , 401    ,30   ,0      ,90         ,"no"         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  , 600    ,30   ,0      ,270         ,"no"         , "Fila"    ,       30     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        20     ),
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,       20     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        10     ),
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,       10     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        1     ),
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,         1     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        2     ),
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,         2     ),

                ("BloqueVerde"  , 50  ,600   ,10  ,None   ,90         ,None         , "Fila"    ,       0      ), ]
    

    """
            
            Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ 
                ❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑
                         Δ       Δ       Δ Δ
                         Δ       Δ       Δ Δ
    ............❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑

    """

    # Descripcion 201 : Tunel de la ternera=


                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner3 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       9     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
            ▮         ▯     
            ▮         ▯     
            ▯       Δ ▮      
            ▯       Δ ▮      
    ...............................................
    """

    Spawner301 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),

                ("PinchoAzul"   , 50  , 550    ,4   ,1      ,0         ,None         , "Columna"    ,       9     ),

                 ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,      16     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
           ◄ ▯       Δ ▮     
           ◄ ▯       Δ ▮     
           ◄ ▮       Δ ▯      
           ◄ ▮       Δ ▯      
    ...............................................
    """

    

    Spawner302 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       9     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
            ▮       Δ ▯     
            ▮       Δ ▯     
            ▯       Δ ▮      
            ▯       Δ ▮      
    ...............................................
    """



    Spawner303 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       9     ),
    
                ("PinchoRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       16     ),
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
             ▯       Δ ▮     
             ▯       Δ ▮     
            Δ▮         ▯      
            Δ▮         ▯      
    ...............................................
    """

    Spawner304 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       9     ),
                ("PinchoAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       16     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
           ◄▮       ◅ ▯     
           ◄▮       ◅ ▯     
            ▯       ◅ ▮      
            ▯       ◅ ▮      
    ...............................................
    """



    Spawner305 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       9     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       16     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
          ◅ ▮       ◄ ▯     
          ◅ ▮       ◄ ▯     
          ◅ ▯         ▮      
          ◅ ▯         ▮      
    ...............................................
    """

    Spawner306 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       9     ),
                ("PinchoAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       16     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
          ◄ ▮       ◄ ▯     
          ◄ ▮       ◄ ▯     
            ▯         ▮      
            ▯         ▮      
    ...............................................
    """

    Spawner307 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       16     ),
                ("PinchoRosa"   , 50  , 550    ,4   ,0      ,0         ,None         , "Columna"    ,       16     ),
                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
          ◅ ▮         ▯     
          ◅ ▮         ▯     
          ◅ ▯         ▮      
          ◅ ▯         ▮      
    ...............................................
    """

                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner308 = [ ("BloqueVerde" , 50   , 600   ,20  ,None   ,90        ,None         , "Fila"       ,        0      ),
                
                ("BloqueAzul"   , 50  , 550    ,2   ,1      ,0         ,None         , "Columna"    ,       8     ),
                ("BloqueRosa"   , 50  , 450    ,2   ,0      ,0         ,None         , "Columna"    ,       8     ),

                ("PinchoAzul"   , 50  , 550    ,4   ,1      ,0         ,None         , "Columna"    ,       9     ),
                

                ("BloqueAzul"   , 50  , 450    ,2   ,1      ,0         ,None         , "Columna"    ,       15     ),
                ("BloqueRosa"   , 50  , 550    ,2   ,0      ,0         ,None         , "Columna"    ,       15     ),
                 ]
    

    """
            ▯       Δ ▮     
            ▯       Δ ▮     
            ▮       Δ ▯      
            ▮       Δ ▯      
    ...............................................
    """


                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner4 = [ ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90        ,None         , "Fila"    ,        0      ),
                ("BloqueAzul"   , 50  , 600    ,7   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,7   ,0      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueAzul"   , 50  , 600    ,7   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,7   ,0      ,90         ,None         , "Fila"    ,        0     ),

                ("BloqueAzul"   , 50  , 452    ,7   ,1      ,90         ,"no"       , "Fila"    ,          28     ),
                ("BloqueRosa"   , 50  , 452    ,7   ,0      ,90         ,"no"         , "Fila"    ,        21     ),
                ("BloqueAzul"   , 50  , 402    ,7   ,1      ,90         ,"no"         , "Fila"    ,        14     ),
                ("BloqueRosa"   , 50  , 402    ,7   ,0      ,90         ,"no"         , "Fila"    ,        7     ),

                ("PinchoVerde"   , 50  , 780    ,28   ,0      ,270         ,"no"         , "Fila"    ,       28     ),
    
            
                ("PinchoRosa"   , 50  , 402    ,7   ,0      ,270         ,"no"         , "Fila"    ,      21     ),
                ("PinchoAzul"   , 50  , 402    ,7   ,1      ,270         ,"no"         , "Fila"    ,      28     ),
                ("PinchoRosa"   , 50  , 450    ,7   ,0      ,90         ,"no"         , "Fila"    ,       14     ),
                ("PinchoAzul"   , 50  , 450    ,7   ,1      ,90         ,"no"         , "Fila"    ,       7     ),

                ("BloqueVerde"  , 50  , 600    ,5  ,None   ,90         ,None         , "Fila"    ,       0      ) ]
                

    """
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ❑❑❑❑❑❑❐❐❐❐❐
                ❑❑❑❑❑❑❐❐❐❐❐ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ


    ............❑❑❑❑❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """

    # Descripcion zzz


    Spawner401 = [ ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90        ,None         , "Fila"    ,        0      ),
                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,None         , "Fila"    ,        0     ),

                ("BloqueAzul"   , 50  , 452    ,3   ,1      ,90         ,"no"       , "Fila"    ,          12     ),
                ("BloqueRosa"   , 50  , 452    ,3   ,0      ,90         ,"no"         , "Fila"    ,        9     ),
                ("BloqueAzul"   , 50  , 402    ,3   ,1      ,90         ,"no"         , "Fila"    ,        6     ),
                ("BloqueRosa"   , 50  , 402    ,3   ,0      ,90         ,"no"         , "Fila"    ,        3     ),    
            
                ("PinchoRosa"   , 50  , 402    ,3   ,0      ,270         ,"no"         , "Fila"    ,      9     ),
                ("PinchoAzul"   , 50  , 402    ,3   ,1      ,270         ,"no"         , "Fila"    ,      12     ),
                ("PinchoRosa"   , 50  , 450    ,3   ,0      ,90         ,"no"         , "Fila"    ,       6     ),
                ("PinchoAzul"   , 50  , 450    ,3   ,1      ,90         ,"no"         , "Fila"    ,       3     ),

                ("BloqueVerde"  , 50  , 600    ,5  ,None   ,90         ,None         , "Fila"    ,       0      ) ]
                

    """
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ❑❑❑❑❑❑❐❐❐❐❐
                ❑❑❑❑❑❑❐❐❐❐❐ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ


    ............❑❑❑❑❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """

     # Descripcion zzz pero mas corto

    Spawner402 = [ ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90        ,None         , "Fila"    ,        0      ),
                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,None         , "Fila"    ,        0     ),

                ("BloqueAzul"   , 50  , 452    ,3   ,1      ,90         ,"no"       , "Fila"    ,          12     ),
                ("BloqueRosa"   , 50  , 452    ,3   ,0      ,90         ,"no"         , "Fila"    ,        9     ),
                ("BloqueAzul"   , 50  , 402    ,3   ,1      ,90         ,"no"         , "Fila"    ,        6     ),
                ("BloqueRosa"   , 50  , 402    ,3   ,0      ,90         ,"no"         , "Fila"    ,        3     ),    
            
                ("PinchoRosa"   , 50  , 402    ,3   ,0      ,270         ,"no"         , "Fila"    ,      9     ),
                ("PinchoAzul"   , 50  , 402    ,3   ,1      ,270         ,"no"         , "Fila"    ,      12     ),
                ("PinchoRosa"   , 50  , 450    ,3   ,0      ,90         ,"no"         , "Fila"    ,       6     ),
                ("PinchoAzul"   , 50  , 450    ,3   ,1      ,90         ,"no"         , "Fila"    ,       3     ),

                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,None         , "Fila"    ,        0     ),
                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,None         , "Fila"    ,        0     ),

                ("BloqueAzul"   , 50  , 452    ,3   ,1      ,90         ,"no"       , "Fila"    ,          12     ),
                ("BloqueRosa"   , 50  , 452    ,3   ,0      ,90         ,"no"         , "Fila"    ,        9     ),
                ("BloqueAzul"   , 50  , 402    ,3   ,1      ,90         ,"no"         , "Fila"    ,        6     ),
                ("BloqueRosa"   , 50  , 402    ,3   ,0      ,90         ,"no"         , "Fila"    ,        3     ),    
            
                ("PinchoRosa"   , 50  , 402    ,3   ,0      ,270         ,"no"         , "Fila"    ,      9     ),
                ("PinchoAzul"   , 50  , 402    ,3   ,1      ,270         ,"no"         , "Fila"    ,      12     ),
                ("PinchoRosa"   , 50  , 450    ,3   ,0      ,90         ,"no"         , "Fila"    ,       6     ),
                ("PinchoAzul"   , 50  , 450    ,3   ,1      ,90         ,"no"         , "Fila"    ,       3     ),
                

                ("BloqueVerde"  , 50  , 600    ,5  ,None   ,90         ,None         , "Fila"    ,       0      ) ]
                

    """
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ❑❑❑❑❑❑❐❐❐❐❐
                ❑❑❑❑❑❑❐❐❐❐❐ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ


    ............❑❑❑❑❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """


     # Descripcion zzz pero mas largo

                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner5 = [ 
                ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90         ,None         , "Fila"       ,         0      ),
                ("BloqueAzul"   , 50  , 600    ,10  ,1      ,270       ,None         , "Columna"      ,        -1     ),
                ("PinchoVerde"  , 50  , 780    ,50  ,1      ,270           ,None         , "Fila"    ,        0      ),

                ("BloqueAzul"   , 50  , 403    ,1   ,1      ,90         ,None         , "Columna"    ,        45     ),
                ("BloqueAzul"   , 50  , 203    ,1   ,1      ,90         ,None         , "Columna"    ,        45     ), 
                ("PinchoAzul"   , 50  , 153    ,1   ,1      ,270        ,None         , "Columna"    ,        45     ),#Parte 1

                ("BloqueAzul"   , 50  , 700    ,1   ,1      ,90         ,None         , "Columna"    ,        41     ), 
                ("BloqueAzul"   , 50  , 400    ,1   ,1      ,90         ,None         , "Columna"    ,        41     ),
                ("PinchoAzul"   , 50  , 350    ,1   ,1      ,270        ,None         , "Columna"    ,        41     ),#Parte 2


                ("BloqueRosa"   , 50  , 400    ,1   ,0      ,90         ,None         , "Columna"    ,        35     ),
                ("BloqueRosa"   , 50  , 200    ,1   ,0      ,90         ,None         , "Columna"    ,        35     ), #Parte 1
                ("PinchoRosa"   , 50  , 150    ,1   ,0      ,270         ,None         , "Columna"    ,       35     ),

                ("BloqueRosa"   , 50  , 600    ,10   ,0      ,180       ,None         , "Columna"    ,        32     ),  # COLUMNA


                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        31     ), #Parte 2
                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        30     ),
                ("BloqueRosa"   , 50  , 750    ,1   ,0      ,90         ,None         , "Columna"    ,        29     ),
                ("BloqueRosa"   , 50  , 402    ,1   ,0      ,90         ,None         , "Columna"    ,        30     ),
                ("PinchoRosa"   , 50  , 352    ,1   ,0      ,270        ,None         , "Columna"    ,        30     ),


                ("BloqueVerde"  , 50  , 600    ,15  ,None   ,90         ,"no"         , "Fila"    ,           25      ), ]
                
    

    """
                  Δ     Δ    Δ      Δ 
                  ❑    ❑    ❑     ❑
        ???

    ............  ❑    ❑    ❑     ❑          ❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """

                #tipo             x     y     num   estado rotacion    fliping         fila o columna   distancia a restar
    Spawner501 = [ 
                ("BloqueVerde"  , 50  , 600    ,10  ,None   ,90         ,None         , "Fila"       ,         0      ),
                ("PinchoVerde"  , 50  , 780    ,60  ,1      ,270       ,"si"         , "Fila"    ,        0      ),

                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,"no"         , "Fila"    ,        57     ),

                ("BloqueRosa"   , 50  , 600    ,3   ,0      ,90         ,"no"         , "Fila"    ,        51     ),

                ("BloqueAzul"   , 50  , 600    ,3   ,1      ,90         ,"no"         , "Fila"    ,        45     ),

                ("BloqueRosa"   , 50  , 600    ,5   ,0      ,90         ,"no"         , "Fila"    ,        39     ),

                ("BloqueRosa"   , 50  , 600    ,6   ,0      ,0          ,None         , "Columna"    ,        32     ),
                
                ("BloqueRosa"   , 50  , 700    ,10   ,0      ,90         ,"no"         , "Fila"    ,        30     ),
                ("PinchoRosa"   , 50  , 650    ,1   ,0      ,270         ,"no"         , "Fila"    ,        21     ),

                ("BloqueAzul"   , 50  , 570    ,10   ,1      ,90         ,"no"         , "Fila"    ,        25     ),             
                ("PinchoAzul"   , 50  , 520    ,3   ,1      ,270         ,"no"         , "Fila"    ,        18     ),             

                ("BloqueVerde"  , 50  , 600    ,20  ,None   ,90         ,"no"         , "Fila"    ,           15      ), ]
                
    

    """
                  Δ     Δ    Δ      Δ 
                  ❑    ❑    ❑     ❑


    ............  ❑    ❑    ❑     ❑          ❑❑❐❐❐❐❐❑❑❑❑❑❑❐❐❐❐❐
                ΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔΔ
    """


    Spawner6 =       [ 
                ("BloqueVerde"  , 50  ,600    ,25  ,None   ,90         ,None         , "Fila"    ,       0      ),
                ("PinchoVerde"  , 50  ,550    ,3   ,1      ,270         ,"no"        , "Fila"    ,       5     ),
                ("PinchoVerde"  , 50  ,550    ,3   ,1      ,270         ,"no"        , "Fila"    ,       12     ),
                ("PinchoVerde"  , 50  ,550    ,3   ,1      ,270         ,"no"        , "Fila"    ,       19     ) ]
    

    
    PRUEBAS = [ ("BloqueVerde"  , 50  ,600    ,30  ,None   ,90         ,None         , "Fila"    ,       0      ),
                ("BloqueAzul"   , 50  ,300    ,8   ,1      ,90         ,None         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  ,300    ,8   ,0      ,270        ,None         , "Fila"    ,       30     ),
                ("BloqueAzul"   , 50  ,300    ,8   ,0      ,90         ,None         , "Fila"    ,       30     ),
                ("BloqueRosa"   , 50  ,300    ,8   ,1      ,270        ,None         , "Fila"    ,       30     )]
    

    # notas de creacion :
        # la y cuidado porque el salto puede moverse 2 pixeles y hacer bypass de la colision :(



    # Paredes alternas
    S1 = Spawner1   # Dificil
    S101 = Spawner101  # Facil

    # Pinchos
    S2 = Spawner2   # Medio
    S201 = Spawner201  # Medio

    S3 = Spawner3       # Facil
    S301 = Spawner301
    S302 = Spawner302
    S303 = Spawner303
    S304 = Spawner304
    S305 = Spawner305
    S306 = Spawner306
    S307 = Spawner307


    S4 = Spawner4
    S401 = Spawner401
    S402 = Spawner402  #dificil su puta madre

    S5 = Spawner5   # version 1.0 (no entra, necesita menos v)
    S501 = Spawner501  # ta wapo

    S6 = Spawner6 # El lag no le dejo triunfar


    S = [S1,S101,S2,S201,S3,S301,S302,S303,S304,S305,S306,S307,S4,S401,S402,S501,]

    #Lista por si quiero probar individual (TESTING)
    #S = [S304,S306]

    return S


def generadorModificado(S, indice, mover):


    if indice >= len(S):
        print("Error porque el indice introducido ha sido : " , indice, ", y las partes actuales existentes es de : " , len(S))
        return IndexError

    Spawner = S[indice]

    



    # Variables

    distancia = mover # ir sumando el numero de bloques adjacentes 
    Puestos = 0

    sueloVerdeList = []

    sueloAzulList = []
    sueloAzulInversoList = []

    sueloRojoList = []
    sueloRojoInversoList = []

    # 0 verde, 1 azul, 2 Rojo
    suelo = [ (sueloVerdeList,None) , (sueloAzulList, sueloAzulInversoList ) , (sueloRojoList, sueloRojoInversoList)   ]

    contador = 0

    while contador != len(Spawner):

        Tipo =   Spawner[contador][0]
        spawnx = Spawner[contador][1]
        spawny = Spawner[contador][2]
        Nspawn = Spawner[contador][3]
        BlocState = Spawner[contador][4]
        Rotar = Spawner[contador][5]
        Flip = Spawner[contador][6]

        Colocacion = Spawner[contador][7]
        DistanciaArestar = Spawner[contador][8]

        contador += 1
        index = -1

        #Seleccionar la lista a añadir
        if Tipo == "BloqueVerde" or Tipo == "PinchoVerde" :
            index = 0
            normalOnly = True 

        elif Tipo == "BloqueAzul" or Tipo == "PinchoAzul":
            index = 1
            normalOnly = False
        
        elif Tipo == "BloqueRosa" or Tipo == "PinchoRosa":
            index = 2
            normalOnly = False
        
        nosuma = False

        if Flip == "no":
            nosuma = True
            Flip = None

        if Flip == "si":
            distancia += Nspawn
            continue

        if index == -1:
            print("Error porque el tipo introducido ha sido : " , Tipo)
            return NameError
        


        if Colocacion == "Fila":

            for i in range(Nspawn):

                Info = Bloques(spawnx , spawny , i + distancia - DistanciaArestar , 0 , Tipo , BlocState , Rotar , Flip ) 
                suelo[index][0].append((Info[0],Info[1],Info[2],Info[3],Info[4]))

                if not normalOnly:
                    
                    Info = Bloques(spawnx , spawny , i + distancia - DistanciaArestar , 0 , Tipo , int(not BlocState) , Rotar , Flip ) 
                    suelo[index][1].append((Info[0],Info[1],Info[2],Info[3],Info[4]))
            
            if not nosuma :

                distancia += Nspawn
        
        elif Colocacion == "Columna":

            for i in range(Nspawn):

                Info = Bloques(spawnx , spawny , distancia - DistanciaArestar , -i , Tipo , BlocState , Rotar , Flip ) 
                suelo[index][0].append((Info[0],Info[1],Info[2],Info[3],Info[4]))

                if not normalOnly:
                    
                    Info = Bloques(spawnx , spawny , distancia - DistanciaArestar, -i , Tipo , int(not BlocState) , Rotar , Flip ) 
                    suelo[index][1].append((Info[0],Info[1],Info[2],Info[3],Info[4]))
        

            
        
        Puestos += Nspawn

    ListaGeneral =        suelo[0][0] + suelo[1][0] + suelo[2][0]         #suelo verde + suelo azul         + suelo rosa
    ListaInversaGeneral = suelo[0][0] + suelo[1][1] + suelo[2][1]         #suelo verde + suelo azul inverso + suelo rosa inverso
    VainasTotal = Puestos



    return (ListaGeneral , ListaInversaGeneral , VainasTotal, distancia)




























#EMPIEZO DEL NIVEL
def mainJuego(   kiwi , kmsporHora   ):

    pygame.init()

    # Configuración de la ventana
    width, height = 1000, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mi Primer Juego")



    # Cargar imagen de fondo
    fondo = pygame.image.load(r"fotosPython\frames\frame 1\frame 1 negro.bmp")
    #fondo = pygame.transform.scale(fondo, (width, height))


    # OBJETOS EN PANTALLA

    # RECTANGULO
    rectangulo_color, rectangulo_rect = rectangulo(width,height)

    #PINGUINO
    spawnx = 90     #90
    spawny = 500    #200
    pinguino, pinguino_rect = pinguinoCrear(spawnx,spawny)
    direccion_derecha = True  # Indica la dirección actual del pingüino


    """
    # TODOS LOS BLOQUES
    suelo, Puestos = generador(10)

    ListaGeneral =        suelo[0][0] + suelo[1][0] + suelo[2][0]         #suelo verde + suelo azul         + suelo rosa
    ListaInversaGeneral = suelo[0][0] + suelo[1][1] + suelo[2][1]         #suelo verde + suelo azul inverso + suelo rosa inverso
    VainasTotal = Puestos
    """

    Niveles = []
    ListaGeneral = []
    ListaInversaGeneral = []
    VainasTotal = 0
    distanciaTotal= 0
    distancia = 0






    if kiwi == 1:

        S = Levels()
    
    elif kiwi == 2:

        S = LevelsHardcore()







    for i in range(20):

        LevelSelection = random.randint(0,len(S)-1)

        General,Inversa,vaina,distancia = generadorModificado(S,LevelSelection,distancia)
        distanciaTotal += distancia
        Niveles.append((General,Inversa,vaina,distancia)) 

        ListaGeneral +=        Niveles[i][0]         #suelo verde + suelo azul         + suelo rosa
        ListaInversaGeneral += Niveles[i][1]       #suelo verde + suelo azul inverso + suelo rosa inverso
        VainasTotal +=         Niveles[i][2] 

    



    BloqueActivo = 1 # El azul Empieza Activo (0 seria rosa)


    # OBJETO RANDOM

    #DALE A LA UB
    spawnx = 300
    spawny = 100

    UB, UB_rect , UBposicionXBloque, UBposicionYBloque = ObjetosRandom(spawnx,spawny,0,0,2) # 5 de azul pincho normal
    UBInfo = (UB,UB_rect,UBposicionXBloque,UBposicionYBloque)

    daleAlaUB = True
    tiempo_inicial = pygame.time.get_ticks()





    #VELOCIDAD DE MOVIMIENTO
    velocidad = 1
    numCaidas = 0
    ultimo_movimientoCAGO = 0

    #Desaparecer Objetos
    rip = False

    # Ajustes de gravedad y salto
    gravedad = 1
    velocidad_salto = -3
    velocidad_y = 1
    en_suelo = False
    salto_en_curso = False
    contador_salto = 0

    #Habilitar movimiento horizontal ??? me gusta el pistacho
    porque_si = False

    #Habilitar movimiento bloques
    start = False

    #Presionar v para cambiar estado (1 vez por presion de tecla)
    v_presionada = False

    #Pinguino se muere
    boom = False

    #Piña colada
    piñaColadapuntoExe = True

    # Definir la ruta de la fuente TrueType
    #print(pygame.font.get_fonts())  # todas las fuentes
    #Fuente = pygame.font.get_fonts()
    #fontNumber = random.randint(0,len(Fuente))
    #font_path = "ruta/a/la/fuente.ttf"  # Reemplaza esto con la ruta de tu fuente TrueType
    #font_path = Fuente[fontNumber] # decepcion

    font_path = r"fotosPython\Comic Sans MS.ttf"

    # Definir el tamaño de la fuente
    font_size = 36

    #Cargar la fuente TrueType
    font = pygame.font.Font(font_path, font_size)
    puntuacionInicial = pygame.time.get_ticks()
    Felicidades = 0
    Joder = "score " + "" + str(Felicidades) 
    text_surface = font.render( Joder , True, (0, 255, 0))

    # Bucle principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            elif event.type == pygame.KEYDOWN: #presionar la tecla

                if event.key == pygame.K_UP and en_suelo:
                    # Iniciar el salto si estamos en el suelo

                    velocidad_y = -3 #direccion contraria
                    en_suelo = False
                    salto_en_curso = True
                    altura = -4
                    contador_salto = 0

            elif event.type == pygame.KEYUP: #dejar de presionar la tecla

                if event.key == pygame.K_UP and salto_en_curso:
                    # Detener el salto si se libera la tecla de salto
                    salto_en_curso = False

                if event.key == pygame.K_v:
                    v_presionada = False
            



        #print(pygame.mouse.get_pos())
        

        
        #velocidad negativa sube 
        if salto_en_curso:


            """

            pinguino_rect.y += altura
            contador_salto += 1

            if contador_salto >= 5: #5 saltos con -4 de movimiento
                altura = -3
            
            if contador_salto >= 12: # 7 saltos con -3 de movimiento
                altura = -2

            if contador_salto >= 62: # 20 saltos con -2 de movimiento
                altura = -1

            if contador_salto >= 222 : # 40 saltos con -1 de movimiento
                altura = 0

            #print(pinguino_rect.y, altura, contador_salto)

            if contador_salto >=500:
                salto_en_curso = False

            
            """
            pinguino_rect.y += -2
            contador_salto += 1

            numCaidas = 0

            if contador_salto >=80:
                salto_en_curso = False

            """
            if not salto_en_curso and not en_suelo:

                numCaidas += 1
                

                tiempo_entre_movimientos = 10  # Tiempo en milisegundos
                ahoraCAIGOXD = pygame.time.get_ticks()

                if ahoraCAIGOXD - ultimo_movimientoCAGO > tiempo_entre_movimientos:

                    ultimo_movimientoCAGO = ahoraCAIGOXD

                    if numCaidas < 30:

                        pinguino_rect.y += 2

                    else :

                        pinguino_rect.y += 1
                
                while pinguino_rect.y % 10 != 0:
                    pinguino_rect.y +=1

            """

        else:     

            """
            tiempo_entre_movimientos = 10  # Tiempo en milisegundos
            ahoraCAIGOXD = pygame.time.get_ticks()

            if ahoraCAIGOXD - ultimo_movimientoCAGO > tiempo_entre_movimientos:

                ultimo_movimientoCAGO = ahoraCAIGOXD
            """

            #gravedad
            velocidad_y += gravedad # siempre caera a velocidad maxima de 1
            en_suelo = False

            if velocidad_y >= 2:
                velocidad_y = 1
            


            pinguino_rect.y += velocidad_y #subir cada vez mas lento y bajar
            

    








        if boom:

            with open(r"fotosPython\score.txt.txt", 'r+') as file:
                # Lee todo el contenido del archivo en una cadena
                contenido = file.read()
                contenido = int(contenido)

               
                if Felicidades > contenido:
                    print("Nuevo Record !" )
                    print("Record anterior --- > ", contenido)
                    print("Nuevo Record --> ", Felicidades )

                    #print("se ha guardado --> ", Felicidades , ", pero como string se ve : ", str(Felicidades) )
                    file.seek(0)
                    file.truncate() # eliminar el contenido para evitar concatenacion

                    file.write(str(Felicidades))


            if Felicidades < 500:
                print("malisimo")
                xd()
                return -500
            elif Felicidades > 1500:
                print("Menos mal : ", Felicidades)
            else:
                print("resultado final :" ,Felicidades)
            return 2


        cooldown_puntuacion = 700  # Tiempo en milisegundos
        willyre = pygame.time.get_ticks()

        if willyre - puntuacionInicial > cooldown_puntuacion:

            puntuacionInicial = willyre
            # Renderizar texto en una superficie
            text_surface = font.render( Joder , True, (0, 255, 0))

            if kmsporHora > 4:
                Felicidades += 100
            else:
                Felicidades += 50
            Joder = "score " + "" + str(Felicidades)
            # Copiar la superficie de texto en la pantalla























        # MOVIMIENTO DE LOS BLOQUES


        teclas = pygame.key.get_pressed()
        
        if start:

            velocidadBloque = kmsporHora

            tiempo_entre_movimientos = 5  # Tiempo en milisegundos
            ahora = pygame.time.get_ticks()

            if ahora - ultimo_movimiento > tiempo_entre_movimientos:

                ultimo_movimiento = ahora

                for i in range(VainasTotal):

                    ListaGeneral[i][1].x -= velocidadBloque
                    ListaGeneral[i] = list(ListaGeneral[i])
                    ListaGeneral[i][3] -= velocidadBloque

                    if ListaInversaGeneral[i][4] != "BloqueVerde":  #sino el verde va a *2 de velocidad

                        if  ListaInversaGeneral[i][4] != "PinchoVerde":

                            ListaInversaGeneral[i][1].x -= velocidadBloque
                            ListaInversaGeneral[i] = list(ListaInversaGeneral[i])
                            ListaInversaGeneral[i][3] -= velocidadBloque
                    
                    









        if teclas[pygame.K_c]:
            porque_si = True


























        # CAMBIO EN LOS BLOQUES
                
        if teclas[pygame.K_v] and not v_presionada :

            v_presionada = True
            en_suelo = False

            BloqueActivo = int (not BloqueActivo)





















        # MOVIMIENTO DEL PINGUINO


        # Obtener el estado del teclado
        velocidadx = 1
        velocidady = 2

        # Actualizar la posición del pinguino según las teclas presionadas
        if teclas[pygame.K_LEFT]:
            if porque_si:
                if direccion_derecha:  # Cambiar de dirección solo si es necesario
                    pinguino = pygame.transform.flip(pinguino, True, False)
                    direccion_derecha = False
                pinguino_rect.x -= velocidadx
            
        if teclas[pygame.K_RIGHT]:
            if porque_si:
                if not direccion_derecha:  # Cambiar de dirección solo si es necesario
                    pinguino = pygame.transform.flip(pinguino, True, False)
                    direccion_derecha = True
                pinguino_rect.x += velocidadx

        if teclas[pygame.K_DOWN]:
            pinguino_rect.y += velocidady































        # COLISION ENTRE OBJETOS



        # PINGUINO CON RECTANGULO
        if pinguino_rect.colliderect(rectangulo_rect):
            print("¡Colisión!")
            rip = True
            rectangulo_rect.x = -100000
            rectangulo_rect.y = -100000
        

        """
        # PINGUINO CON BLOQUES Verdes
        for i in range(numBlocsVerds):
            if pinguino_rect.colliderect(sueloVerdeList[i][1]):
                #print("¡Colisión 2!")
                #pinguino_rect.y = velocidad_y
                pinguino_rect.y = sueloVerdeList[i][1].y - pinguino_rect.height
                en_suelo = True
        """


        #PINGUINO CON BLOQUES VARIABLES (BLOQUES Y PINCHOS)
        for i in range(VainasTotal):

            if ListaGeneral[i][4] == "BloqueVerde":

                if pinguino_rect.colliderect(ListaGeneral[i][1]):
                    #print("¡Colisión 2!")
                    #pinguino_rect.y = velocidad_y
                    pinguino_rect.y = ListaGeneral[i][1].y - pinguino_rect.height
                    en_suelo = True
            
            elif ListaGeneral[i][4] == "PinchoVerde":

                SuperPosicion = pinguino_rect.colliderect(ListaGeneral[i][1].inflate(-10, -10))

                if SuperPosicion:
                    boom = True
                    pinguino_rect.x = 10000


            else:


                if BloqueActivo == 1: # Azul

                    AktivBloc = "BloqueAzul"
                    AktivPinchito = "PinchoAzul"
                
                elif BloqueActivo == 0: # Rosa

                    AktivBloc = "BloqueRosa"
                    AktivPinchito = "PinchoRosa"


                if ListaGeneral[i][4] == AktivBloc:

                    # CABEZA PINGUINO CON TECHO
                    condicion1 = pinguino_rect.y == ListaGeneral[i][1].y + ListaGeneral[i][1].height    #PORQUE NO FUNCIONA COMO ANTES?????????? (EL +1 SOBRA PORQUE ARRIBA NO ESTA???)
                    condicion3 = ListaGeneral[i][1].x <= pinguino_rect.x + pinguino_rect.width <= ListaGeneral[i][1].x + ListaGeneral[i][1].width # que la esquina derecha esta dentro del rango del blqoue
                    #if  condicion1 and condicion2 and condicion3 :

                    #if condicion1: print("hola") ; pygame.time.delay(50)
                    #if condicion3: print("2222222222222222222") ; pygame.time.delay(100)

                    if condicion1 and condicion3: # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                        salto_en_curso = False # detenemos salto
                        #print("valleta vieja")
                        velocidad_y = 0


                    # DERECHA PINGUINO CON IZQUIERDA DEL BLOQUE
                        
                    condicion1 = pinguino_rect.x + pinguino_rect.width == ListaGeneral[i][1].x
                    condicion3 = ListaGeneral[i][1].y <= pinguino_rect.y + pinguino_rect.height / 2 <= ListaGeneral[i][1].y + ListaGeneral[i][1].height

                    if condicion1 and condicion3:
                        #print("boom")
                        pinguino_rect.x = 1700
                        boom = True

                    
                    # Izquierda PINGUINO CON IZQUIERDA DEL BLOQUE
                        
                    condicion1 = pinguino_rect.x  == ListaGeneral[i][1].x + ListaGeneral[i][1].width
                    condicion3 = ListaGeneral[i][1].y <= pinguino_rect.y + pinguino_rect.height / 2 <= ListaGeneral[i][1].y + ListaGeneral[i][1].height

                    if condicion1 and condicion3:
                        #print("boom")
                        pinguino_rect.x = 1700
                        boom = True




                    # PIE PINGUINO CON SUELO
                    condicion1 = pinguino_rect.y + pinguino_rect.height  == ListaGeneral[i][1].y  #que la cabeza del pinguino toca la parte de abajo
                    condicion3 = ListaGeneral[i][1].x <= pinguino_rect.x + pinguino_rect.width <= ListaGeneral[i][1].x + ListaGeneral[i][1].width # que la esquina derecha esta dentro del rango del blqoue

                    SuperPosicion = pinguino_rect.colliderect(ListaGeneral[i][1].inflate(-5, -5))

                    #if (condicion1 and condicion3) : # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                    if pinguino_rect.colliderect(ListaGeneral[i][1]): # no se pero funciona fuck it
                        #salto_en_curso = False # detenemos salto
                        en_suelo = True # estamos en el foking suelo
                        pinguino_rect.y = ListaGeneral[i][1].y - pinguino_rect.height   # no lo movemos
                        #print("Condicion de tocar hierba")
                        #velocidad_y = 0               

                    # INTERIOR CON OTRO INTERIOR

                    #if condicion1 and condicion3: # al venir solo por la derecha los bloques no hace falta la 2 (que si no no va xd)
                    if SuperPosicion : # no se pero funciona fuck it
                        pinguino_rect.x = 1700
                        #print("BUUUUUUUUUUUUM")
                        boom = True

                elif ListaGeneral[i][4] == AktivPinchito:

                    SuperPosicion = pinguino_rect.colliderect(ListaGeneral[i][1].inflate(-10, -10))

                    if SuperPosicion:
                        boom = True
                        pinguino_rect.x = 10000

            























        # COLISION TECHO Y SUELO


        # SUELO PANTALLA
        if pinguino_rect.y >= height - pinguino_rect.height:
            pinguino_rect.y = height - pinguino_rect.height
            boom = True
            en_suelo = True

        # TECHO PANTALLA
        if pinguino_rect.y <= 0:
            pinguino_rect.y = 0
            velocidad_y = 0  # Detener el movimiento hacia arriba cuando toca el techo











        # INFINIDAD DEL NIVEL
            
        
        if VainasTotal < 150:

            Niveles = []
            distancia = 50

            for i in range(10):

                LevelSelection = random.randint(0,len(S)-1)

                General,Inversa,vaina,distancia = generadorModificado(S,LevelSelection,distancia)
                distanciaTotal += distancia
                Niveles.append((General,Inversa,vaina,distancia)) 

                ListaGeneral +=        Niveles[i][0]         #suelo verde + suelo azul         + suelo rosa
                ListaInversaGeneral += Niveles[i][1]       #suelo verde + suelo azul inverso + suelo rosa inverso
                VainasTotal +=         Niveles[i][2] 
    

















        # FONDO + OBJETOS

        #cambiar el tamaño de forma dinamica (tiembla la pantalla!!)
        a = 0
        b = 0
        #window = pygame.display.set_mode((width + a, height + b))



        #usar la imagen de fondo
        window.blit(fondo, (0, 0))

        #imprimir objetos
        if rip: #rectangulo desaparecido
            pygame.draw.rect(window, rectangulo_color, rectangulo_rect)
        window.blit(pinguino, pinguino_rect)

        container = 0

        eliminar = []
        contandoFuera = 0

        #imprimir todos los bloques
        for i in range(VainasTotal-1,-1,-1):

            i -= contandoFuera  #evitar index out of range

            if ListaGeneral[i][4] == "BloqueVerde" or ListaGeneral[i][4] == "PinchoVerde" : # Azul

                if ListaGeneral[i][1].x < width: # - 100:
                        window.blit(ListaGeneral[i][0],ListaGeneral[i][1])
                        container += 1


            elif BloqueActivo == 1: # Azul (SE IMPRIME LA LISTA NORMAL)

                if ListaGeneral[i][1].x < width: # - 100:
                        window.blit(ListaGeneral[i][0],ListaGeneral[i][1])
                        container += 1
                
            
            
            elif BloqueActivo == 0: # Rojo (SE IMPRIME LA LISTA INVERSA)

                if ListaInversaGeneral[i][1].x < width: # - 100:
                        window.blit(ListaInversaGeneral[i][0],ListaInversaGeneral[i][1])
                        container += 1



            #bloque a la izquierda, bloque que no volvera a aparecer
            if ListaGeneral[i][1].x < -50:

                ListaGeneral.pop(i)
                ListaInversaGeneral.pop(i)
                VainasTotal -= 1
                contandoFuera += 1



        #print(VainasTotal)

        tiempo_actual = pygame.time.get_ticks()

        # Reproducir el sonido después de 5 segundos (5000 milisegundos)
        if tiempo_actual <= 4000:
            window.blit( UBInfo[0], UBInfo[1]  )


        #score
        window.blit(text_surface, (700,50))
        # Actualizar la pantalla
        pygame.display.flip()
        

        #pygame.time.delay(500)


        #Delay de 2 segundos para empezar el juego
        if piñaColadapuntoExe:
            if tiempo_actual - tiempo_inicial >= 2000:   # CAMBIAR
                #pygame.time.delay(2000) # 5000 pistachos
                piñaColadapuntoExe = False
                start = True
                ultimo_movimiento = pygame.time.get_ticks()


    pygame.quit()




async def main():    
    
    erenoeleccion = MENU()

    while erenoeleccion != 1:

    

        if erenoeleccion == 2:
            xd()

        elif erenoeleccion == 3:
            mainJuego(2,4)
        else:
            mainJuego(2,6) # modo sexo

        erenoeleccion = MENU()

    await asyncio.sleep(0)

    #pincho, bloques 2
    #salir 1
    #sexo 0
        
        
asyncio.run(main())





# COSAS A MEJORAR
        
"""


QUE AL CREAR UN BLOQUE DENTRO DEL METODO SE CREE SU INVERSO Y DEVUELVA AMBOS ROLLO (INFO NORMAL), (INFO INVERSA) --> MENOS CODIGO
HACER QUE EL MENU TENGA EL CODIGO NORMAL   (ME DIO PALO)
MEJORAR SALTO
USAR CLASES


AÑADIR MUSICA
AÑADIR FONDO DINAMICO (YA EN ARCHIVOS)
"""