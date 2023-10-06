import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from os import unlink

df = pd.read_csv('data.csv')
lista = df.to_numpy().tolist()

for i in lista:
    persona=i[2] + " " + i[1]

    try:
        img=mpimg.imread('fotos/' + persona + '.jpg')
        if len(img.shape)!=3:
            print(persona, "Esta foto no es a color")
    except Exception as ex:
        print(persona, "No tiene foto")
        lista.remove(i)

def mostrarJugadores():
    #obtengo una posicion
    j = 1
    #recorro la lista
    for i in lista:
        #creo un subplot de 3 x 4
        plt.subplot(3, 4, j)
        #obtengo la imagen
        img=mpimg.imread('fotos/' + i[2] + " " + i[1] + '.jpg')
        #cfg de la imagen
        plt.imshow(img)
        plt.title(i[1])
        plt.axis('off')
        j += 1
        #si llego a dimaria sale
        if i[1] == 'di maria':
            break
    #muestro las imagenes
    plt.show()
    init()


def mostrarJugador():
    n = input("Ingrese el nombre del jugador: ")
    for i in lista:
        if i[0] == n:
            #obtengo el indice
            indice = lista.index(i)
            #obtengo al jugador
            persona = lista[indice][2] + " " + lista[indice][1]
            #obtengo la imagen
            img=mpimg.imread('fotos/' + persona + '.jpg')
            #muestro la imagen
            plt.imshow(img)
            plt.show()
            init()

    print("Mostrar jugador")

def eliminarJugador():
    global df
    n = input("Ingrese el nombre del jugador a eliminar: ")
    a = input("Ingrese el apellido del jugador a eliminar: ")

    #borro la foto
    unlink('fotos/' + n + " " + a + '.jpg')
    #borro el jugador del csv
    for i in lista:
        if i[2]==n and i[1]==a:
            camiseta = i[0]
            lista.remove(i)
    
    df = df[df.num!=camiseta] #elimino la fila del csv
    df.to_csv('data.csv') #guardo el csv
    print("Jugador eliminado: " + n + " " + a)
    init()

def exit():
    return print("Adios")

def init():
    op = input("¿Que desea hacer?\n1. Mostrar jugadores\n2. Mostrar jugador\n3. Borrar un jugador\n 4. Salir\n")
    if op == "1":
        mostrarJugadores()
    elif op == "2":
        mostrarJugador()
    elif op == "3":
        eliminarJugador()
    elif op == "4":
        exit()
    else:
        print("Opcion no valida")
        init()
init()

