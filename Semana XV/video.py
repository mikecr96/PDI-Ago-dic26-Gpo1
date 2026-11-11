import cv2 as cv

cap = cv.VideoCapture(1) # Normalmente es 0
if not cap.isOpened():
    print('No se pudo inicializar la cámara')
    exit()

while True:
    _, frame = cap.read()
    frame = cv.resize(frame, (300, 300))
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.blur(frame_gray, (15, 15))
    frame_gray = cv.Canny(frame_gray, 50, 100)
    cv.imshow('Webcam', frame_gray)
    if cv.waitKey(33) == ord('q'): break

cap.release()
cv.destroyAllWindows()