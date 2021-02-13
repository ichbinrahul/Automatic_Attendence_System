import cv2 as cv
import numpy as np
import os

class Trainer:
    def __init__(self,classes):
        try:
            self.classes = classes
            self.haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
            self.class_list = os.listdir(os.path.join(os.getcwd(),"Class-List"))
            self.features = []
            self.labels = []
            self.path = os.path.join(os.getcwd(), "Class-List")
            self.exc_list = [f"{self.classes}-trained.yml", f"{self.classes}-features.npy", f"{self.classes}-labels.npy"]
            self.face_recognizer = cv.face.LBPHFaceRecognizer_create()
            os.mkdir(f"{self.path}\{self.classes}\Files")
            self.trained_files_list = os.listdir(f"{self.path}\{self.classes}\Files\\")
        except FileExistsError:
            pass

    def train_model(self):
        student_list = os.listdir(os.path.join(self.path,self.classes))
        if "Files" in student_list:
            student_list.pop(student_list.index("Files"))
        if "Output" in student_list:
            student_list.pop(student_list.index("Output"))
        try:
            for student in student_list:
                path = os.path.join(os.path.join(self.path,self.classes), student)
                label = student_list.index(student)

                for img in os.listdir(path):
                    img_path = os.path.join(path, img)
                    
                    img_array = cv.imread(img_path)
                    gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

                    faces_rect = self.haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=2)

                    for (x,y,z,h) in faces_rect:
                        faces_roi= gray[y : y+h, x : x+h]
                        self.features.append(faces_roi)
                        self.labels.append(label)
        except (FileExistsError, cv.error) as ex:
            if self.exc_list[0] in self.trained_files_list:
                os.remove(f"{self.path}\{self.classes}\Files\{self.classes}-trained.yml")
            if self.exc_list[1] in self.trained_files_list:
                os.remove(f"{self.path}\{self.classes}\Files\{self.classes}-features.yml")
            if self.exc_list[2] in self.trained_files_list:
                os.remove(f"{self.path}\{self.classes}\Files\{self.classes}-labels.yml")
    
    def start_trainer(self):
        try:
            self.train_model()

            self.features = np.array(self.features, dtype="object")
            self.labels = np.array(self.labels)

            self.face_recognizer.train(self.features, self.labels)
            
            print(f"\nTraining done for {self.classes}\n")

            self.face_recognizer.save(f"{self.path}\{self.classes}\Files\{self.classes}-trained.yml")
            np.save(f"{self.path}\{self.classes}\Files\{self.classes}-features.npy", self.features)
            np.save(f"{self.path}\{self.classes}\Files\{self.classes}-labels.npy", self.labels)

        except (NotADirectoryError, FileNotFoundError, cv.error) as e:
            if self.exc_list[0] in self.trained_files_list:
                os.remove(f"{self.path}\{self.classes}\Files\{self.classes}-trained.yml")
            if self.exc_list[1] in self.trained_files_list:
                os.remove(f"{self.path}\{self.classes}\Files\{self.classes}-features.npy")
            if self.exc_list[2] in self.trained_files_list:
                os.remove(f"{self.path}\{self.classes}\Files\{self.classes}-labels.npy")

            self.face_recognizer.save(f"{self.path}\{self.classes}\Files\{self.classes}-trained.yml")
            np.save(f"{self.path}\{self.classes}\Files\{self.classes}-features.npy", self.features)
            np.save(f"{self.path}\{self.classes}\Files\{self.classes}-labels.npy", self.labels)
            print(f"\nTraining done for {self.classes}\n")