
# Face Recognition Attendance System

This desktop application aims to simplify the process of Attendance Management of different classes and batches using Face Recognition and user-friendly GUI. The management of data and marking of attendance is carried out in Excel files
## About

This python based app uses OpenCV libraries: face detection using Haar feature-based cascade classifier and face recognition using Local Binary Patterns Histograms (LBPH) . GUI features are implemented using tkinter library.
## Technologies Used

1.Tkinter for whole GUI.

2.OpenCV for taking images and face recognition (cv2.face.LBPHFaceRecognizer_create())

3.Mysql is used for creating Database.

4.CSV, Numpy, Pandas, datetime etc. for other purposes.


## Installation

Requirements for the project:

```bash
  pip install pillow
``` 
```bash
  pip install opencv-python
```   
```bash
  pip install numpy
```

## Project Flow and Explanation

- When we run main.py ,the main window will open with several choices.
- Then click student details and window will open asking all details .
- After entering all the datails click on save button so that all information is saved to database , then click on details shown in right side and then click on take photo sample.
- By clicking Take photo sample , the camera will open and it starts taking an image sample of the person.It takes 100 images as a sample and stores them in folder TrainingImage.After completion, it notifies that pictures saved.
- After taking the image sample, go back and then we have to click the Train Data button. It takes a few seconds to train the machine for the images taken by clicking the Take Image button and creating a classifier.xml file and store in the data folder.
- Now all initial setups are done. By clicking the Detect Face button camera of the running machine is opened again. If the system recognizes the face, then Id, roll number, department and Name of person are shown on Image.
- After quitting it, attendance of person will be stored in the Attendance folder as CSV file with name, id, department, roll number, date, and time and it is also available in the Attendance window.