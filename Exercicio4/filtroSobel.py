import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('Imagem/neymar.jpg')

# Redimensionar a imagem
largura = 500  # nova largura
altura = 300   # nova altura
imagem_redimensionada = cv2.resize(imagem, (largura, altura))

img_gray = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_RGB2GRAY)

img_sobelx = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
img_sobely = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)
#img_sobelxy = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) #assim fica fraco
img_sobelxy = cv2.addWeighted(img_sobelx, 0.5, img_sobely, 0.5, 0) #melhor usar assim

# Nomear as imagens 
cv2.putText(img_sobelxy, " Sobel",(10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

# Mostrar a imagem combinada
cv2.imshow('Imagem', img_sobelxy)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()