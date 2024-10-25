import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('Imagem/paisagem.jpg')

# Redimensionar a imagem
largura = 500  # nova largura
altura = 300   # nova altura
imagem_redimensionada = cv2.resize(imagem, (largura, altura))

# Converter as imagens
imagem_gray = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)  # Escala de cinza
imagem_rgb = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2RGB)    # RGB
imagem_hsv = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2HSV)    # HSV

# Converter a imagem ma 
imagem_gray_3canais = cv2.cvtColor(imagem_gray, cv2.COLOR_GRAY2BGR)

# Converter a imagem HSV de volta para BGR para visualização
imagem_hsv_bgr = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

# Nomear as imagens 
cv2.putText(imagem_gray_3canais, 'Escala de Cinza', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(imagem_rgb, 'RGB', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(imagem_hsv_bgr, 'HSV', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
cv2.putText(imagem_redimensionada, 'Original', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

# Concatenar as imagens
linha1 = np.hstack((imagem_gray_3canais, imagem_rgb))
linha2 = np.hstack((imagem_hsv, imagem_redimensionada))
imagens_comb = np.vstack((linha1, linha2))

# Mostrar a imagem combinada
cv2.imshow('Imagem', imagens_comb)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()