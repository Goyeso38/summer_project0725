import cv2
import mediapipe as mp

img_path = "day1_4.jpg"
img = cv2.imread(img_path)
h, w, c = img.shape


mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(
  model_selection = 0,
  min_detection_confidence = 0.5)

src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results = face_detection.process(src)

if results.detections:
  for det in results.detections:
    bbox = det.location_data.relative_bounding_box
    x = int(bbox.xmin * w)
    y = int(bbox.ymin * h)
    bbox_w = int(bbox.width * w)
    bbox_h = int(bbox.height * h)

    cv2.rectangle(img, 
                  (x, y), (x + bbox_w, y + bbox_h),
                  (0, 255, 0), 2)


cv2.imshow("얼굴 인식 결과", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("test3.jpg", img)