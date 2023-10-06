#VAMOS A HACER UN CLASIFICADOR DE IMAGENES (FRUTAS)

import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import time

categorias = ["ananas", "kiwis", "manzanas"]
imagenes = []
labels = []
size = (200,200)

x=0
#EXTRACCION DE DATOS

for i in categorias:
    c=1
    for k in range(10):
        img = cv2.imread(i+"/"+str(c)+".jpg", 0)
        img = cv2.resize(img, size)
        img=np.asarray(img)
        imagenes.append(img)
        c+=1
        labels.append(x)
    x=x+1

#CREACION DEL MODELO

modelo = tf.keras.models.Sequential([
    tf.keras.layers.conv2D(32,(3,3), activation="relu", input_shape=(200,200,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.conv2D(64,(3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=100, activation="relu"),
    tf.keras.layers.Dense(units=3, activation="softmax")
])

#OPTIMIZAR EL MODELO

modelo.compile(optimizer="adam",
                loss="sparse_categorical_crossentropy",
                metrics=["accuracy"])

#ENTRENAMIENTO DEL MODELO

modelo.fit(np.array(imagenes), np.array(labels), epochs=20)

#PRUEBA DEL MODELO

test = cv2.imread("test.jpg", 0)
test = cv2.resize(test, size)
test = np.asarray(test)
test = np.array([test])

resultado = modelo.predict(test)
print(resultado)

print("Manzana: ", resultado[0][0]*100, "%")
print("Anana: ", resultado[0][1]*100, "%")
print("Kiwi: ", resultado[0][2]*100, "%")