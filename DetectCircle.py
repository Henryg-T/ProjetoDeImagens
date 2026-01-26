import cv2
import numpy as np

img = cv2.imread("Ligthning Control.jpeg")

# Converter pra cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#Converte para tons de cinzas

# Blur ajuda MUITO
gray = cv2.GaussianBlur(gray, (9, 9), 1.5)# ajuda na nitidez removendo ruidos e pequenos detalhes

# Detectar círculos
circulos = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,#precisao e detalhamento
    minDist=300,#distancia min entre os circulos
    param1=100,#bordas
    param2=30,#nivel "confiança"
    minRadius=180,#tamanho varia conforme o tamanho esperado
    maxRadius=260
)

if circulos is None:
    print("Círcle not found")
    exit()

circulos = np.uint16(np.around(circulos))
cx, cy, r = circulos[0][0]

print(f"Centro: ({cx}, {cy}) | Raio: {r}")

cv2.circle(img, (cx, cy), r, (0, 255, 0), 3)
cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)

cv2.imshow("Círculo detect", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
