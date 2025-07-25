from ultralytics import YOLO
import cv2
model = YOLO("yolo11s.pt")

image_path = "test1.jpg"
results = model(image_path, classes = [0])

results[0].save("result2.jpg")

img = results[0].plot()
cv2.imshow("이미지를 보여주는 창", img)
cv2.waitKey(0)
cv2.destroyAllWindows()