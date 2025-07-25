import cv2

image_path = "day1_1.jpg"
image = cv2.imread(image_path)

cv2.imshow("이미지 보여줘", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
