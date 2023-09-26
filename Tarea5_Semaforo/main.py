import cv2
from random import choice

fotos = ["semaforo/1.png", "semaforo/2.png", "semaforo/3.png"]

while True:
    foto = choice(fotos)
    img = cv2.imread(foto)
    cv2.imshow("Semaforo", img)

    c_sup=img[300,253]
    c_med=img[400,253]
    c_inf=img[800,253]

    # El color gris es el 77,77,77
    if c_sup[0] != 77:
        print("Semaforo Rojo - PARAR!")
    elif c_med[0] != 77:
        print("Semaforo Amarillo - PRECAUCION!")
    else:
        print("Semaforo Verde - ADELANTE!")

    cv2.waitKey(5000)
    cv2.destroyAllWindows()



