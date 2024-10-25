import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('Imagem/neymar.jpg')

# Redimensionar a imagem
largura = 500  # nova largura
altura = 300   # nova altura
imagem_redimensionada = cv2.resize(imagem, (largura, altura))

blur_img = cv2.blur(imagem_redimensionada, (15, 15))

# Nomear as imagens 
cv2.putText(blur_img, " ",(10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

# Mostrar a imagem combinada
cv2.imshow('Imagem', blur_img)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()