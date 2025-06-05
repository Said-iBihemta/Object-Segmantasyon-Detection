import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO("sirken_best.pt")

# Giriş ve çıkış video yolu
input_path = "input_video.mp4"
output_path = "output_video.mp4"

# Video oku
cap = cv2.VideoCapture(input_path)

# Video özelliklerini al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Video çerçevelerini işle
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model.predict(source=frame, conf=0.25, save=False)
    annotated_frame = results[0].plot()
    out.write(annotated_frame)
frame_count = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model.predict(source=frame, conf=0.25, save=False)
    annotated_frame = results[0].plot()
    out.write(annotated_frame)
    frame_count += 1


cap.release()
out.release()
print(f"Toplam yazılan frame sayısı: {frame_count}")
print(f"✅ İşlem tamamlandı. Çıktı: {output_path}")
