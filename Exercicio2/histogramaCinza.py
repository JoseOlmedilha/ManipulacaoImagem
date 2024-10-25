import cv2 

import matplotlib.pyplot as plt 

import numpy as np 

# Carregue a imagem RGB 

imagem = cv2.imread('Imagem/neymar.jpg', 0) 

# Calcular o histograma
histograma  = cv2.calcHist([imagem], [0], None, [256], [0, 256]) 


# Plotar o histograma
plt.figure()
plt.title("Histograma da Imagem em Escala de Cinza")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
plt.plot(histograma)
plt.xlim([0, 256])
plt.show()

equ = cv2.equalizeHist(imagem)  # Equaliza o histograma


# Calcular o histograma
histograma2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

# Plotar o histograma
plt.figure()
plt.title("Histograma da Imagem em Escala de Cinza")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
plt.plot(histograma2)
plt.xlim([0, 256])
plt.show()
res = np.hstack((imagem, equ))  # Combina a imagem original e a equalizada lado a lado

cv2.imshow(res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Conveter as imagens 
##imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Escala de cinza

##imagem_gray_3canais = cv2.cvtColor(imagem_gray, cv2.COLOR_GRAY2BGR)
#imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)    # RGB
#imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)    # HSV






