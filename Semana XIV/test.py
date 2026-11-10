import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lena = cv.imread('/Users/miguelcamargorojas/iCloud Drive (Archive)/Documents/UP/PDI-Ago-dic26/PDI-Ago-dic26-Gpo1/images/lena.jpg', 0)
media = np.mean(lena)
lena_bin = cv.threshold(lena, media, 1, cv.THRESH_BINARY)[1]
lena_neg = 255 - lena
# plt.imshow(lena_bin, 'gray')
# plt.show()
cv.imshow(f'Lena negativo', lena_neg)
while True:
    tecla = cv.waitKey(0)
    if tecla == ord('q'):
        print("Presionaste la q")
        exit()
    elif tecla == ord('b'): print("Presionaste la b")
    elif tecla == ord('c'): print("Presionaste la c")
    elif tecla == ord('d'): print("Presionaste la d")
    elif tecla == ord('e'): print("Presionaste la e")
    # else: print("NO Entré al if")

# print(ord('q'))