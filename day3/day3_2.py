from ultralytics import solutions
import cv2

counter = solutions.ObjectCounter(
  show=True,
  model="yolo11s.pt",
  classes = [0],
  region = [ (20,20), (500,20), (500,500), (20,500)]
)


video_path = "cctv2.mp4"
cap = cv2.VideoCapture(video_path)


while cap.isOpened():
  ret, img = cap.read()
  if ret:
    results = counter(img)

    if cv2.waitKey(30) == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()