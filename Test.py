import cv2
import numpy as np
import os

# 1. Carregar a imagem
image = cv2.imread('Ligthning Control.jpeg')
output = image.copy()

# 2. Converter para escala de cinza (essencial para HoughCircles)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Aplicar suavização (Blur) para reduzir ruído e evitar falsos círculos
gray_blurred = cv2.medianBlur(gray, 5)

# 4. Detectar círculos usando HoughCircles
circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,  # Distância mínima entre os centros dos círculos
    param1=50,  # Limite superior do detector de bordas Canny
    param2=30,  # Limite do acumulador (menor = mais círculos falsos)
    minRadius=10,  # Raio mínimo
    maxRadius=100  # Raio máximo
)

# 5. Desenhar os círculos detectados
if circles is not None:
    # Converter coordenadas e raio para inteiros
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        # Desenhar o contorno do círculo
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        # Desenhar o centro do círculo
        cv2.circle(output, (x, y), 2, (0, 128, 255), 3)

# 6. Mostrar resultado
cv2.imshow("Circulos Detectados", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
