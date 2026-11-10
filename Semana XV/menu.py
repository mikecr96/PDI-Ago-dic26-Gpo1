import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lena = cv.imread('/Users/miguelcamargorojas/iCloud Drive (Archive)/Documents/UP/PDI-Ago-dic26/PDI-Ago-dic26-Gpo1/images/lena.jpg')
if lena is None:
    print('No se pudo cargar la imagen')
    exit()
"""
g - grayscale
b - Blur
e - bordes
r - original
s - guardar
q - quit
"""
while True:
    actual = lena.copy()
    cv.imshow('X', actual)

    tecla = cv.waitKey(33)
    if tecla == ord('q'):
        print("Presionaste la q. SALIENDO")
        exit()
    elif tecla == ord('g'):
        print("Presionaste la g. GRAYSCALE")
        actual = cv.cvtColor(lena, cv.COLOR_BGR2GRAY)
    elif tecla == ord('b'): 
        print("Presionaste la b. BLUR")
        actual = cv.blur(lena, (5, 5))
    elif tecla == ord('e'): 
        print("Presionaste la e. BORDES")
        actual = cv.Canny(lena, 20, 100)
    elif tecla == ord('r'): 
        print("Presionaste la r. ORIGINAL")
        actual = lena.copy()
    elif tecla == ord('s'): 
        print("Presionaste la s. GUARDAR")
        cv.imwrite('prueba.png', actual) # Persistencia
    lena = actual

    # else: print("NO Entré al if")
cv.destroyAllWindows()
# print(ord('q'))