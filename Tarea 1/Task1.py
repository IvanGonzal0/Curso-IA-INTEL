import pandas as pd
import matplotlib.pyplot as plt

#  Importar el archivo CSV
df = pd.read_csv('nba.csv')

# Modificar el campo 'nombre' por 'jugador' e imprimir el df
df.rename(columns={'nombre': 'jugador'}, inplace=True)

print(df)

# Pedir la acción al usuario
print("¿Qué deseas hacer?")
print("1. Ver todos los jugadores")
print("2. Ver detalle por jugador")
print("3. Ver el puntaje general")
print("4. Graficar")
opcion = int(input("Ingresa el número de la opción deseada: "))

# Ver todos los jugadores
if opcion == 1:
    nombres_jugadores = df['jugador']   #creo un dataset con los nombres de los jugadores
    print("Nombres de los jugadores:")
    print(nombres_jugadores)            #printeo el dataset que arme solamente con el nombre de jugadores

# Ver detalle por jugador
elif opcion == 2:
    nombre_jugador = input("Ingresa el nombre del jugador: ")   #input para el usuario
    jugador_info = df[df['jugador'] == nombre_jugador]          #busco en el df en la columna jugador los valores que sean == a lo que ingresa el usuario
    print(jugador_info)                                         #print del jugador escrito por el usuario

#  Ver el puntaje general (media de puntos)
elif opcion == 3:
    media_puntos = df['puntos'].mean()                          #creo una variable para guardar el promedio de la columna "puntos" del df orignal
    print(f"El puntaje general promedio es: {media_puntos}")    #print con funcion para imprimir la media obtenida con la funcion mean()

#  Graficar puntos por jugador
elif opcion == 4:
    plt.figure(figsize=(10, 10))                        #usando matplotlib seteo el tamaño de la figura a dibujar
    plt.bar(df['jugador'], df['puntos'], color='green') #los valores de los paramatros pertenecen a: plt.bar(x,y, color de barras)
    plt.xlabel('Jugador')                               #en x voy a indicar que son Jugadores
    plt.ylabel('Puntos')                                #en voy a imprimir que son puntos
    plt.title('Puntos por Jugador')                     #seteo el titulo de la figura
    plt.xticks(rotation=45)                             #roto los valores de x para que no se superpongan entre si
    plt.tight_layout()                                  #ajusto los margenes y espacios entre elementos de la figura con esta funcion
    plt.show()                                          #ploteo
else:
    print("Opción inválida")