# Automatic Attendence System
Automatic Attendance System is designed to collect and manage student’s attendance records from video camera devices installed in a class rooms. Based on the verification of student identity in the video feed, attendance will be updated in a .csv file so that the data can be exported into excel files.

## Abstract
To maintain a discipline and let students grasp utmost knowledge in schools, colleges and universities the attendance system is introduced. There are two conventional techniques to mark attendance of students in a particular class. One of them is by calling the roll number and the second is to take students sign on a piece of paper against their roll number. Hence there was a need to evolve this system in such a way that it could become user friendly, less time consuming and efficient. This is an automated system to assist the faculty in taking attendance of the whole class without any disturbance or time waste. The idea can encompass a large number application one of which include face identification, it will help save time and efficiently identifies and eliminates the chances of proxy attendance. The main purpose of this project is to develop an automated attendance system that can run on user’s laptop providing the user attendance of the class.
This system can be implemented in any field where laptop/desktop or even a Raspberry Pi is present. In addition, as the project objectives and the design criteria all met, it’s greatest to say this project is an engineering solution for all university and colleges to track and manage the attendance. Due to Command Line Interface of the system, the entire process is accelerated. The CLI is also designed in such a way it is easy for even first time CLI users. Since the application built uses python with open sourced libraries the application is highly portable. The above application can run on a medium powered android smartphone also with “Termux” with python interpreter installed in it.

![Camera Setup](https://github.com/ichbinrahul/Automatic_Attendence_System/blob/main/images/camerasetup.jpg?raw=true)
*Picture 1: Camera Setup required for the system (Source: Google)*
![Training Workflow](https://github.com/ichbinrahul/Automatic_Attendence_System/blob/main/images/workflow.png?raw=true)
*Picture 2: Process Flow (Source: Google)*

## Keywords
Attendance, Face identification, Face recognizer, OpenCV.

## Methodology
In this part we will use a method that will give an overview of the approach to our project and the ways it should be done. As the previous work was not enough which led us to the development in this project in the most feasible and efficient way possible.
The face detection module for this project is Viola jones algorithm (Haar Cascade) to detection from the video feed while registering student and save their facial features for further detection. For recognition of students during class sessions the project implements face recognition with LBPH and required video processing using OpenCV. Since lot of images are required to train the Haar Cascade generated features file, we implemented a function, it takes in an image and generates more images by applying transforms, changing color spaces of images.

![Main Screen](https://github.com/ichbinrahul/Automatic_Attendence_System/blob/main/images/main.png?raw=true)
*Picture 3: Main Screen of application (Source: Tested on PC)*
![Generated Images](https://github.com/ichbinrahul/Automatic_Attendence_System/blob/main/images/generatedimages.png?raw=true)
*Picture 4: Generated Images (Source: Tested on PC)*

The model of the attendance monitoring system and how it will be implemented in a particular class. As we can see that there is also a teacher’s desk who will be facing the students hence he will not be considered as a student. A camera is setup in the middle of the class room at a suitable height to get the full view of the class till the last bench. After the students have been seated. The camera will take an image and starts the process of face detection using the techniques and methods discussed in the methodology section. After this the program will automatically make a folder in the database having the students to be recognized. The already placed images of each student is taken and used from database for image recognition. The images will be fetched and compared with each of the entry in the database and hence will be checked whether the student is present in the class or not. If there is no match the program will move on to the next picture.
![Face Recognition output](https://github.com/ichbinrahul/Automatic_Attendence_System/blob/main/images/recognition.png?raw=true)
*Picture 5: Real time face recognition (Source: Tested on PC)*
![Output files](https://github.com/ichbinrahul/Automatic_Attendence_System/blob/main/images/output.png?raw=true)
*Picture 6: Output files (Source: Tested on PC)*

## Hardware and Software Requirement
Camera, Basic computer (laptop, desktop, or any single board computer), Python interpreter with required libraries.

## Tools and Package Sources
* [HaarCascadefrontalfacealt - haarcascade_frontalface_alt.xml](https://github.com/opencv/opencv/tree/master/data/haarcascades)
* [Python 3.9.1](https://www.python.org/)
* [OpenCV](https://pypi.org/project/opencv-python/)
