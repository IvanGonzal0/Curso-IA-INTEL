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
    nombres_jugadores = df['jugador']
    print("Nombres de los jugadores:")
    print(nombres_jugadores)

# Ver detalle por jugador
elif opcion == 2:
    nombre_jugador = input("Ingresa el nombre del jugador: ")
    jugador_info = df[df['jugador'] == nombre_jugador]
    print(jugador_info)

#  Ver el puntaje general (media de puntos)
elif opcion == 3:
    media_puntos = df['puntos'].mean()
    print(f"El puntaje general promedio es: {media_puntos}")

#  Graficar puntos por jugador
elif opcion == 4:
    plt.figure(figsize=(10, 10))
    plt.bar(df['jugador'], df['puntos'], color='green')
    plt.xlabel('Jugador')
    plt.ylabel('Puntos')
    plt.title('Puntos por Jugador')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Opción inválida")