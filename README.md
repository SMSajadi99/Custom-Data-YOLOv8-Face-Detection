# Custom-Data-YOLOv8-Face-Detection

## Installation
YOLOv8 released a package named “ultralytics”, that you can install with the mentioned command below.
```
pip install ultralytics
```
## Preparation
By cloning the data, we can have the overall structure, we can prepare this item with the following command: (of course, we will tell another method for preparation in the last part)
```
!git clone https://github.com/SMSajadi99/Custom-Data-YOLOv8-Face-Detection.git
```
## Start Training
You can start training YOLOv8 on custom data by using mentioned command below in the terminal/(command prompt).
```
yolo task=detect mode=train model=yolov8n.pt data=custom.yaml epochs=3 imgsz=640
```
* task = detect (It can be segment or classify)

* mode = train (It can be predict or val)

* model = yolov8n.pt (It can yolov8s/yolov8l/yolov8x)

* epochs = 3 (It can be any number)

* imgsz = 640 (It can be 320, 416, etc, but make sure it needs to be a multiple of 32)

## Result
![d41b9bcf-9cd2-4478-9654-e16cc03a8e9a](https://github.com/SMSajadi99/Custom-Data-YOLOv8-Face-Detection/assets/69210109/f42eeca7-4d01-4d62-8da2-5af5c9f7fa11)

