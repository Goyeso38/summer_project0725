from ultralytics import YOLO
from ultralytics import solutions
import cv2


blurrer = solutions.ObjectBlurrer(
    show = True,
    model = "yolo11s.pt",
    classes = [3]
)
image_path = "image1.jpg"

img = cv2.imread(image_path)
results = blurrer(img)

cv2.imshow("result", results.plot_im)
cv2.waitKey(0)

results[0].save("result3.jpg")