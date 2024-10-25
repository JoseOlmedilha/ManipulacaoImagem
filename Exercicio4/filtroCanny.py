import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('Imagem/neymar.jpg')

# Redimensionar a imagem
largura = 500  # nova largura
altura = 300   # nova altura
imagem_redimensionada = cv2.resize(imagem, (largura, altura))

img = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_RGB2GRAY)
img = cv2.GaussianBlur(imagem_redimensionada, (3, 3), 3, 3)
copyimg = imagem_redimensionada.copy()

copyimg = cv2.Canny(img, 0, 300)

# Nomear as imagens 
cv2.putText(copyimg, " Canny",(10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

# Mostrar a imagem combinada
cv2.imshow('Imagem',copyimg)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()