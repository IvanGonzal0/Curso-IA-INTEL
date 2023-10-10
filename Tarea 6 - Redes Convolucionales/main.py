import tensorflow as tf
from tensorflow import keras
from keras import layers,models
import numpy as np
import cv2

categorias = ['ananas', 'kiwis', 'manzanas']

imagenes = []
labels = []
size = (200,200)

# x=0
# for i in categorias:
#     c=1
#     for k in range(10):
#         img = cv2.imread('frutas/'+i+'/'+str(c)+'.jpg', 0 )
#         img = cv2.resize(img, size)
#         imagenes.append(img)
#         labels.append(x)
#         c+=1
#     x+=1

# model = tf.keras.models.Sequential([
#     tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(200,200,1)),
#     tf.keras.layers.MaxPooling2D(2,2),
#     tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
#     tf.keras.layers.MaxPooling2D(2,2),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(units=100, activation='relu'),
#     tf.keras.layers.Dense(units=3, activation='softmax')
#     ])

# model.compile(optimizer='adam',
#                 loss='sparse_categorical_crossentropy',
#                 metrics=['accuracy'])

# imagenes = np.array(imagenes)
# labels = np.array(labels)
# model.fit(imagenes, labels, epochs=20)
# #GUARDO EL MODELO
# models.save_model(model, 'modelo-furtas.keras')

#PRUEBA DEL MODELO

test=cv2.imread('frutas/test.jpg', 0)
test=cv2.resize(test, size)
test=np.array(test)
test=np.array([test])


# # CARGO EL MODELO
modelo = models.load_model('modelo-furtas.keras')
resultado=modelo.predict(test)


print(resultado)

print("Manzana: ", resultado[0][0]*100, "%")
print("Anana: ", resultado[0][1]*100, "%")
print("Kiwi: ", resultado[0][2]*100, "%")