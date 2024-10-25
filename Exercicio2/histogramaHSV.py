
import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('Imagem/neymar.jpg')

# Converter para o espaço de cor HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Separar os canais
canal_h, canal_s, canal_v = cv2.split(imagem_hsv)

# Calcular os histogramas
hist_h = cv2.calcHist([canal_h], [0], None, [256], [0, 256])
hist_s = cv2.calcHist([canal_s], [0], None, [256], [0, 256])
hist_v = cv2.calcHist([canal_v], [0], None, [256], [0, 256])

# Plotar os histogramas
plt.figure()
plt.title("Histogramas HSV")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
plt.plot(hist_h, color='r', label='Hue')
plt.plot(hist_s, color='g', label='Saturation')
plt.plot(hist_v, color='b', label='Value')
plt.xlim([0, 256])
plt.legend()
plt.show()
