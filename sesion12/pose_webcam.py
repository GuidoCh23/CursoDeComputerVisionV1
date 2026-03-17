import cv2
from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = "best.pt"

model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(0)
# Pueden usar la app IP Webcam de google play para simular su dispositivo movil como una camara wifi http o rstp
#cap = cv2.VideoCapture("http://192.168.18.42:8080/video")
if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la camara")

print("Pose estimation en camara. Presiona 'q' para salir.")

cv2.namedWindow("Pose Estimation", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.25, verbose=False)
    annotated = results[0].plot()

    cv2.imshow("Pose Estimation", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
