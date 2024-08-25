import os
import csv
import time
from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt') 
threshold = 0.5
cap = cv2.VideoCapture(0)

log_path = os.path.join('.', 'detection_log.csv')
with open(log_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp','count'])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    class_counts = {
        'person': 0,
        'cell phone': 0
    }
    with open(log_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                label = results.names[int(class_id)]
                if(label == 'person' or label == 'cell phone'):
                    class_counts[label] += 1
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                writer.writerow([timestamp,class_counts])
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('YOLOv8 Live Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
