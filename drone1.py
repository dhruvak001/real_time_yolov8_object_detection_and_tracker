import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import Tracker
import os

# Load the trained YOLO model
model = YOLO('yolov8s.pt')

# Define your class list for six classes
#class_list = ['class0', 'class1', 'class2', 'class3', 'class4', 'class5']
my_file = open("yolo_tracker/coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 

# Define your class list for six classes
#class_list = ['class0', 'class1', 'class2', 'class3', 'class4', 'class5']

# Tracker instance
tracker = Tracker()
reported_ids = []

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

def process_frame(frame):
    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    list = []
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        if d >= len(class_list):
            print(f"Warning: Detected class ID {d} is out of range for class_list.")
            continue  # Skip this detection if class ID is out of range
        c = class_list[d]
        list.append([x1, y1, x2, y2, d])  # Include the class id in the list
    bbox_id = tracker.update([bbox[:4] for bbox in list])  # Pass only bbox coordinates
    for bbox in bbox_id:
        x3, y3, x4, y4, obj_id = bbox
        cx = (x3 + x4) // 2
        cy = (y3 + y4) // 2
        cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
        cv2.circle(frame, (cx, cy), 3, (255, 0, 255), -1)
        cv2.putText(frame, str(obj_id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        if obj_id not in reported_ids:
            send_location(obj_id)  # Function to send GPS location
            reported_ids.append(obj_id)
        else:
            print(obj_id, "- already sent")
    return frame

def send_location(obj_id):
    print("locaation sent - ", obj_id)
    # Implement the logic to send GPS location to the ground station
    pass

# Case 1: Video Feed from the Camera
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = process_frame(frame)
        cv2.imshow("RGB", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# Case 2: Sequence of Images/Frames
def process_images(image_folder):
    images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()  # Sort images by name to ensure sequential processing
    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        frame = process_frame(frame)
        cv2.imshow("RGB", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

# Uncomment the appropriate function call based on your input type
# process_video('path/to/your/video.mp4')
process_images('/Users/sanjay/Documents/autosky/dataset/test')
