# Real-Time Object Tracking and Line Crossing Detection using YOLO and Centroid Tracking
The project involves using a YOLO (You Only Look Once) model for object detection in video frames or sequences of images, coupled with a custom object tracker to maintain the identities of detected objects across frames. The application is designed to process frames from a video feed or a sequence of images, detect objects, track them, and potentially send the locations of newly identified objects to a ground station...

## Key Components
* YOLO Model: Utilizes the YOLOv8 model for object detection.
* Tracker: Maintains object identities across frames based on the object's center positions.
* Frame Processing: Integrates the YOLO model and tracker to process each frame and display the results.
* Can input a series of frames ot video on depending on the input.
* Edit the Send Loaction function according to your needs
  
## File Structure
* drone1.py: Main script for processing video or image sequences.
* tracker.py: Contains the Tracker class for maintaining object identities.

## Dependencies
* OpenCV: For handling image and video processing.
* pandas: For handling detection data.
* ultralytics: For loading and using the YOLO model.
* os: For file handling.
### Instructions for Running the Project
Prerequisites
* Python: Ensure Python 3.7 or higher is installed.
* YOLOv8: Install the ultralytics package for YOLO models.
* OpenCV: Install OpenCV for image and video processing.
* Pandas: Install Pandas for data handling.

bash-
`pip install ultralytics opencv-python pandas`

### Setting Up the Project
* Clone the Repository:</br>
`git clone https://github.com/your-username/drone-object-tracking.git`</br>
`cd drone-object-tracking`

* Ensure the YOLO model file is available:<br/>
 Place yolov8s.pt in the project directory or specify the correct path.

* Prepare Class List:<br/>
Ensure that the coco.txt file, containing class names for YOLO, is placed in the yolo_tracker directory.

### Running the Code
* Processing a Video File:<br/>
Uncomment the line in drone.py related to video processing and specify the path to your video file:<br>
`process_video('path/to/your/video.mp4`

* Processing a Sequence of Images:<br/>
Uncomment the line in drone.py related to image processing and specify the path to your image folder:</br>
`process_images('/path/to/your/images')`

* Execute the Script:<br/>
`python drone1.py`

## Conclusion
This project demonstrates a practical application of deep learning for real-time object detection and tracking using YOLOv8 and a custom tracking algorithm. The detailed instructions and code ensure you can easily set up and run the project to process video feeds or sequences of images for object tracking and location reporting.






