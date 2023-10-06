import cv2
from random import choice

fotos = ["1.png", "2.png", "3.png"]

while True:
    #Elegimos una foto al azar
    foto = choice(fotos)
    #Leemos la foto
    img = cv2.imread(foto)
    #Mostramos la foto
    cv2.imshow("Detector de color en el semaforo", img)
    #Esta es la ubicacion del color en la foto
    c_sup=img[300,253]
    c_med=img[400,253]
    c_inf=img[800,253]
    #Si el color no es gris, entonces es rojo, amarillo o verde dependendiendo la posicion
    # El color gris es el 77,77,77
    if c_sup[0] != 77:
        print("Semaforo Rojo - PARAR!")
    elif c_med[0] != 77:
        print("Semaforo Amarillo - PRECAUCION!")
    else:
        print("Semaforo Verde - ADELANTE!")

    key = cv2.waitKey(3000)

    # Romper el bucle si se presiona la tecla Escape (ESC)
    if key == 27:
        break

cv2.destroyAllWindows()


