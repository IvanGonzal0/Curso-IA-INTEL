# Import de librerias a utilizar
import tensorflow as tf
from tensorflow import keras
import pandas as pd

# Creacion de las capas
capa1 = tf.keras.layers.Dense(units=3,input_shape=[1])
capa2 = tf.keras.layers.Dense(units=3)
capasalida = tf.keras.layers.Dense(units=1)

# Creacion del modelo secuencial
model = tf.keras.Sequential([oculta1, oculta2, capasalida])
# Parametros de compilación
model.compile(optimizer= "Nadam", loss = "mean_squared_error")

# Lectura de los datos, desde un csv utilizando pandas
df = pd.read_csv("ejercicio3_clima.csv")
df.head()

# Extraer los datos para almacenarlos en arrays
years = []
temps = []

# Recorremos el df en la columna year
for i in df['year']:
  years.append(i)

# Recorrer el df en la columna temp
for i in df['temp']:
  temps.append(i)

# Entrenar el modelo
model.fit(years,temps, epochs=100)

# Predecir la temperatura en el año ...

input = int(input("Ingrese año a predecir: "))
print(model.predict([input]))