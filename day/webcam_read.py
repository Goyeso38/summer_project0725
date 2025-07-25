import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow("영상을 보여주는 창", img)
        else:
            break

        if cv2.waitKey(30) == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()