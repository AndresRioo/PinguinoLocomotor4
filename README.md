# PinguinoLocomotor4

hola :)

Codigo del juego en python 


NOTAS A TENER EN CUENTA 

El codigo del menu y el del propio juego son diferentes (el menu me daba palo optimizarlo)
Hace falta descargar la libreria pygame y alguna otra.
quico puter0

COMO AÑADIR SECCIONES PERSONALIZADAS

en el metodo LevelsHardcore() añadir/cambiar una lista.

Si quieres cambiar solo edita el contenido y revisa que esa lista este en uso
Si quieres añadir crea una nueva y metela en la lista del final

COMO CREAR UN NIVEL NUEVO

Las listas ya creadas tendran esta estructura:

#tipo --> el bloque que quieras, poner bien el string. Si es azul que su estado sea 1 y si es rosa que sea 0
#x --> recomendable que sea 50. (si quieres manejar la distancia con la coordenada cada bloque mide 50 pixeles asi que poner multiples de 50)
#y --> la altura que quieras
#num --> numero de bloques a poner
#fliping/no suma --> 
·si es None --> si esta en estado fila , la cantidad de num sera sumada a la distancia 
·si es "no" --> no se suma a la distancia
·si es "si" --> solo suma a la distancia (no se pone el bloque)
#fila o columna --> si los num bloques se ponen en fila o columna. Las columnas no suman distancia
#distancia a restar --> relativamente donde va el bloque

para entender donde poner los bloques piensa que la posicion x=50 es donde aparece el primer bloque
por cada bloque en estado fila que se ponga la distancia se sumara en 50 para que el siguiente bloque aparezca despues. Si no restas ninguna distancia todos se pondran despues del anterior.
Por eso restas.

Mejor probarlo para entenderlo

                #tipo             x     y     num   estado rotacion  fliping/no suma  fila o columna   distancia a restar
    Spawner201 = [("BloqueVerde"  , 50  ,600   ,10  ,None   ,90         ,"no"         , "Fila"    ,       0      ), #poner 10 bloques verdes  (.......)
                ("BloqueVerde"  , 50  ,600   ,40  ,None   ,90         ,"si"         , "Fila"    ,       0      ),  #sumas 40 bloques a la distancia relativa

              "Ahora mismo la distancia relativa donde irian los bloques es de 40 y tengo 10 bloques verdes y 30 espacios vacios

              ❑❑❑❑❑❑❑❑❑ (verde)   - - - - - - - - - - - - - - - (vacio)    [] (puntero que marca la distancia relativa) 


                ("BloqueRosa"   , 50  , 401    ,30   ,0      ,90         ,"no"         , "Fila"    ,       30     ),  #la fila de arriba (❑❑❑)   le resto 30 al puntero para indicar donde empieza la colocacion 
                ("BloqueRosa"   , 50  , 600    ,30   ,0      ,270         ,"no"         , "Fila"    ,       30     ), #la fila de abajo  (❑❑❑) 

                al restarle 30 al puntero empiezo a poner los 30 bloques 30 posiciones antes del puntero (justo despues de los verdes)
                si no restara 30 quedaria asi

                ❑❑❑❑❑❑ (Verde) ------------------- (30 de Vacio) ❑❑❑❑❑❑❑❑(Rosa)

                pero como resto 30

                ❑❑❑❑❑❑ (Verde) ❑❑❑❑❑❑❑❑❑❑❑❑ (Rosa)

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        20     ), pincho izquierda
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,       20     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        10     ), pincho medio
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,       10     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        1     ), pinchos derecha
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,         1     ),

                ("PinchoRosa"   , 50  ,550    ,1   ,0      ,270        ,"no"          , "Columna"    ,        2     ),
                ("PinchoRosa"   , 50  ,450    ,1   ,0      ,90        ,"no"          , "Columna"    ,         2     ),

                ("BloqueVerde"  , 50  ,600   ,10  ,None   ,90         ,None         , "Fila"    ,       0      ), ]   bloques verdes finales
    

    """
            
            Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ Δ 
                ❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑
                         Δ       Δ       Δ Δ
                         Δ       Δ       Δ Δ
    ............❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑❑

    """
