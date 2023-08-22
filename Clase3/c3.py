import random as rd
from random import randint, choice   

# numeros=[1,3,5,3,7,88]

# print(rd.randint(1,10)) #randint nos devuelve un numero aleatorio dentro de un rango determinado
# print(choice(numeros))  #choice me devuelve un random que se encuentre dentro de la lista


poblacion = 5   #creamos 5 individuos a esos individuos se les van a asignar atributos (fuerza,intelegincia,agilidad)
seleccion = 2   #esta va a ser la cantidad de individuos seleccionados (se eligen los que tengan mejores states de fuerza, int, agi)
generaciones = 3    #aca vamos a crear 3 generaciones con los mejores individuos

# para la seleccion vamos a hacer un algoritmo genetico que seleccione los mejores individuos

individuos = []
# hago un for para crear la cantidad de individuos y se asigno sus atributos aleatoriamente
for i in range(poblacion):
    fuerza = rd.randint(1,3)
    vel = rd.randint(1,3)
    altura = rd.randint(1,3)

    aptitud = fuerza+vel+altura #este atributo es el que define al mejor(definiendo que la suma de los 3 atributos define cual es el mejor)
    individuo=[fuerza,vel,altura,aptitud]
    individuos.append(individuo)

print("La primer generacion de individuos es: " , individuos)

# aca vamos a seleccionar a los 2 mejores, basandonos en la aptitud 
seleccionados=[]

def seleccionar():
    
    for i in range(seleccion):
        max = 0
        #aca busco el que tenga mejor aptitud por indice
        for i in individuos:
            if i[3]>max:
                max=i[3]
                indice = individuos.index(i)
        seleccionados.append(individuos[indice])    #aca lo agregamos a la lista seleccionados
        individuos.pop(indice)                   #aca eliminamos ese registro para que no se pueda repetir en el proximo bloque

    print(f'Los seleccionados son: {seleccionados}')


#vacio la lista individuos de nuevo

def heredar():
    global individuos
    individuos=[]
    
    for i in range(poblacion):
        fuerza = seleccionados[rd.randint(0,1)][0]
        vel = seleccionados [rd.randint(0,1)][1]
        alto = rd.randint(1,3)

        aptitud = fuerza+vel+alto
        individuo = [fuerza, vel, alto, aptitud]
        individuos.append(individuo)

    print(f'Los seleccionados son: {individuos}')

for i in range(generaciones-1):

    seleccionar()
    heredar()





if seleccionados[0][3] > seleccionados[1][3]:
    print("El mejor individuo es: ", seleccionados[0])
else:
    print("El mejor individuo es: ", seleccionados[1])