import time
import os
import csv
from ultralytics import YOLO
import cv2

model = YOLO('Multiple_Person_Phone_Detection/yolov8n.pt') 

threshold = 0.5
video_path = 'C:/Users/aranu/Desktop/Minor_Combined/Input_Data/video.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
    exit()

log_path = os.path.join('.','Multiple_Person_Phone_Detection', 'MPPD.csv')
with open(log_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'count'])

while True:
    ret, frame = cap.read()
    if not ret:
        break


    millis = cap.get(cv2.CAP_PROP_POS_MSEC)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(millis / 1000.0))

    results = model(frame)[0]
    class_counts = {
        'person': 0,
        'cell phone': 0
    }

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            label = results.names[int(class_id)]
            if label in class_counts:
                class_counts[label] += 1

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {score:.2f}", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

    with open(log_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, class_counts])

    cv2.imshow('YOLOv8 Recorded Video Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
