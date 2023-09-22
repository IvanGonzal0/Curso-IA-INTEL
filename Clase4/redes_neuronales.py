import tensorflow as tf
from tensorflow import keras

entradas=[0,2,4,6,8,10]
salidas=[0,20,40,60,80,100] 

oculta1=tf.keras.layers.Dense(units=3,input_shape=[1])
oculta2=tf.keras.layers.Dense(units=3)
final=tf.keras.layers.Dense(units=1)

modelo=tf.keras.Sequential([oculta1,oculta2,final])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1),loss="mean_squared_error")

modelo.fit(entradas,salidas,epochs=200)



valor=int(input("Ingrese un valor: "))

resultado=modelo.predict([valor])
print(resultado)