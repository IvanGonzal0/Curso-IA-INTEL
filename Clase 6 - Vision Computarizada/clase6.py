import cv2


img = cv2.imread('stop.png')
#img_gris = cv2.imread('stop.png', 0) #con el 0 se lee la imagen directamente en blanco y negro
#gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#print(img.shape)
#img_chica = cv.resize(img, (200,200))   #achico la imagen a 200px x 200px

#cv2.imshow("stop", img_gris) #stop es el nombre de la ventana, y el segundo parametro es la imagen
#cv2.waitKey(3000)       #waitkey es el tiempo que se muestra la imagen
#cv2.destroyAllWindows() #cierra todas las ventanas para que no quede nada abierto en segundo plano


# USAR LA WEBCAM
#img_cam=cv2.VideoCapture(0) #este videocapture0 utiliza en 0 la camara por defecto de la computadora

#img_cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#img_cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

#ret, frame = img_cam.read()
#cv2.imshow("Camara", frame)
#cv2.imwrite("mi foto.jpg", frame)
#cv2.waitKey(5000)
#img_cam.release()
#cv2.destroyAllWindows()


(b,g,r) = cv2.split(img)
img[(b==0) & (g==0) & r(r==255)] = 0,0,0
cv2.imshow("cambio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()