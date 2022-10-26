# pip install opencv-contrib-python
# pip install pyqt5

import cv2

# capture image
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('output', frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()