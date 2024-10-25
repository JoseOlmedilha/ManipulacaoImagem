import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregue a imagem RGB
imagem = cv2.imread('Imagem/neymar.jpg')

# Separe os canais R, G e B 
canal_r, canal_g, canal_b = cv2.split(imagem)

# Calcule os histogramas para cada canal
hist_r = cv2.calcHist([canal_r], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([canal_g], [0], None, [256], [0, 256])
hist_b = cv2.calcHist([canal_b], [0], None, [256], [0, 256])

 # Plote os histogramas
plt.rcParams.update({'font.size': 12})
plt.figure(figsize=(5, 10))
plt.subplot(311)
plt.title('Histograma do Canal Vermelho (R)')
plt.xlabel('Valor do Pixel')
plt.ylabel('Frequência')
plt.plot(hist_r, color='red')
plt.subplot(312)
plt.title('Histograma do Canal Verde (G)')
plt.xlabel('Valor do Pixel')
plt.ylabel('Frequência') 
plt.plot(hist_g, color='green')
plt.subplot(313)
plt.title('Histograma do Canal Azul (B)')
plt.xlabel('Valor do Pixel')
plt.ylabel('Frequência')
plt.plot(hist_b, color='blue')
plt.tight_layout()
plt.show()
