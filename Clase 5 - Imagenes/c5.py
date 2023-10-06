import tensorflow as tf
from tensorflow import keras
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img2 = mpimg.imread('M:/Users/compu/Pictures/proyecto/img2.jpg')
img3 = mpimg.imread('M:/Users/compu/Pictures/proyecto/img3.jpg')
#print(img.shape)   #me imprime los datos de imagenes, alto ancho y canales

#Vamos a hacer un subplot de imagenes, el subplot dice que va a ser una matriz de 2x2, y el 1 el primer elemento

plt.subplot(2,2,1)
img1 = mpimg.imread('M:/Users/compu/Pictures/proyecto/img1.jpg')
plt.title("1")
plt.imshow(img1)

plt.subplot(2,2,2)
img1 = mpimg.imread('M:/Users/compu/Pictures/proyecto/img2.jpg')
plt.title("2")
plt.imshow(img1)

plt.subplot(2,2,3)
img1 = mpimg.imread('M:/Users/compu/Pictures/proyecto/img3.jpg')
plt.title("3")
plt.imshow(img1)
plt.show()