import cv2 as cv
import os
import numpy as np
from datetime import datetime

class Marker:
    def __init__(self):
        self.class_name = input("\nEnter Class >> ")
        self.path = os.path.join(os.getcwd(), "Class-List")
        self.haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
        self.face_recognizer = cv.face.LBPHFaceRecognizer_create()
        self.today = datetime.now()
        self.time_date_started = self.today.strftime( "%d-%m-%Y %H(Hour(s))-%M(Minute(s))" )   
        try:
            os.mkdir(f"{self.path}\{self.class_name}\Output")
        except FileExistsError:
            pass    
        try:
            self.features = np.load(f"{self.path}\{self.class_name}\Files\{self.class_name}-features.npy", allow_pickle = True)
            self.labels = np.load(f"{self.path}\{self.class_name}\Files\{self.class_name}-labels.npy")
            self.face_recognizer.read(f"{self.path}\{self.class_name}\Files\{self.class_name}-trained.yml")       
            self.student_list = []
            for student in os.listdir(f"{self.path}\{self.class_name}"):
                self.student_list.append(student)
            if "Files" in self.student_list:
                self.student_list.pop(self.student_list.index("Files"))
            if "Output" in self.student_list:
                self.student_list.pop(self.student_list.index("Output"))
        except (FileNotFoundError, cv.error) as e:
            return False

    def rescaleFrame(self,frame, scale=0.5):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width,height)
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

    def file_writer(self, present_list):
        file_name = str(input("\nEnter name of session >> ")+ " " + self.time_date_started)     
        with open(f"{self.path}\{self.class_name}\Output\{file_name}.csv","w") as file_object:
            for name in present_list:
                file_object.write(f"{name},\n")
            file_object.close()
        return file_name
    
    def start_session(self):
        print("Session Starting. Please wait.......")
        print("Press 'ctrl + c' to exit")
        try:
            video = cv.VideoCapture(0)
            fourcc = cv.VideoWriter_fourcc(*'MJPG')
            frame_width = int(video.get(3))
            frame_height = int(video.get(4))
            out = cv.VideoWriter(f"{self.path}\{self.class_name}\Output\{self.time_date_started}.avi",fourcc, 20.0, (frame_width, frame_height))
            present_list = []
            while video.isOpened():
                ret, frame = video.read()
                if ret:
                    self.rescaleFrame(frame)

                    out.write(frame)

                    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)

                    faces_rect = self.haar_cascade.detectMultiScale(gray,1.1,2)

                    for (x,y,w,h) in faces_rect:
                        faces_roi = gray[y:y+h , x:x+h]

                        label , confidence = self.face_recognizer.predict(faces_roi)

                        present_list.append(self.student_list[label])

                        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
                        cv.putText(frame, str(self.student_list[label]), (x,y) , cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 239, 255), thickness=2)

                        cv.imshow("Live Session", self.rescaleFrame(frame))
                        if cv.waitKey(1) & 0xFF == ('s'):
                            break

        except KeyboardInterrupt:   
            video.release()
            out.release()
            cv.destroyAllWindows()
            if input("Do you keep recored video? ('n' to delete) >> ") == "n":
                os.remove(f"{self.path}\{self.class_name}\{self.time_date_started}.avi")
            present_list_final = []
            for entry in present_list: 
                if entry not in present_list_final: 
                    present_list_final.append(entry)
            file_name = self.file_writer(present_list_final)
            print(f"\nSession ended. Attendence list saved as '{file_name}.txt' in {self.class_name}\\Output folder.\n")