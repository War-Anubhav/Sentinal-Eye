from deepface import DeepFace
import cv2
import csv
import time

reference_img_path = "C:/Users/aranu/Desktop/Minor_Combined/Input_Data/image.jpg"
reference_img = cv2.imread(reference_img_path)
if reference_img is None:
    raise Exception(f"Image not found at {reference_img_path}")

video_path = 'C:/Users/aranu/Desktop/Minor_Combined/Input_Data/video.mp4'  
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise Exception("Failed to open video file")

ans = []
interval = 1 
last_time = 0  

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000 
        if current_time - last_time > interval:
            last_time = current_time
            try:
                result = DeepFace.verify(reference_img, frame, model_name='VGG-Face', detector_backend='opencv')
                
                if result["verified"]:
                    print("detected")
                    ans.append(1)
                else:
                    print("not detected")
                    ans.append(0)

            except Exception as e:
                print(f"not detection")
                ans.append(0)

        cv2.imshow('Face Verification', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()

   
    with open('Face_Recognition/verification_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Detection Confidence'])
        for value in ans:
            writer.writerow([value])
