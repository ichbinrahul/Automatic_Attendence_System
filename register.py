import os
import cv2 as cv
import numpy as np

class Register:
    def __init__(self):
        self.path = ""
        self.to_path = ""

    def make_dir(self):
        class_name = input("Enter Section >> ")
        pwd = os.getcwd()
        self.path = os.path.join(pwd, "Class-List")
        self.path = os.path.join(self.path, class_name)
        try:
            os.mkdir(self.path)
        except FileExistsError:
            print(f"\n{class_name} already exist.\nOpening {class_name} to add more students.\n")


    def obtain_image(self, student_name):
        video = cv.VideoCapture(0)
        while True:
            ret, frame = video.read()
            if ret:
                frame = cv.resize(frame, (int(frame.shape[1]*0.75),int(frame.shape[0]*0.75)))
                alt_frame = frame.copy()

                start = int(alt_frame.shape[1]*0.325) , int(alt_frame.shape[0]*0.25)
                end = int(alt_frame.shape[1]-(alt_frame.shape[1]*0.325)) , int(alt_frame.shape[0]-(alt_frame.shape[0]*0.25))

                alt_frame = cv.putText(alt_frame, "Press 's' to capture image", (start[0] - int(start[0]*0.35), start[1] - int(0.12*start[1])), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0), thickness=2)
                alt_frame = cv.putText(alt_frame, "Align face in center of rectangle", (start[0] - int(start[0]*0.45), end[1] + int(0.085*end[1])), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0), thickness=2)
                cv.rectangle(alt_frame,start, end , (0,255,0), thickness=2)
                cv.imshow("Live Feed",alt_frame)
                if cv.waitKey(1) & 0xFF == ord('s'):
                    cv.destroyAllWindows()
                    cv.imwrite(student_name + ".jpg", frame)
                    cv.imshow("Captured Image", frame)
                    cv.waitKey(0)
                    os.rename("{0}\{1}.jpg".format(os.getcwd(), student_name), "{0}\{1}.jpg".format(self.to_path, student_name))
                    break
        video.release()
        cv.destroyAllWindows()

    def capture_image(self):
        student_name = input("\nEnter Student Name >> ")
        self.to_path = os.path.join(self.path, student_name)
        try:    
            os.mkdir(self.to_path)
            self.obtain_image(student_name)
            print("\nImage Captured Sucessfull \n")
            while input("\nDo you want to retake image? ('y' to retake) >> ") == "y":
                os.remove(f"{self.to_path}\{student_name}.jpg")
                self.obtain_image(student_name)
            to_path = self.to_path
            self.do_transform(to_path, student_name)
        except FileExistsError:
            print(f"\n{student_name}'s entry already exist.\n")
            if not(input("Do you replace image? ('n' to skip) >> ") == "n"):
                to_be_removed = os.listdir(self.to_path)
                for item in to_be_removed:
                    os.remove(f"{self.to_path}\{item}")
                self.obtain_image(student_name)
                self.do_transform(self.to_path, student_name)


    def do_transform(self, to_path, student_name): 
        os.chdir(to_path)
        
        def translate(img, x, y):
            transMat = np.float32([[1,0,x],[0,1,y]])
            dimensions = (img.shape[1], img.shape[0])
            return cv.warpAffine(img, transMat, dimensions)
        
        def change_clrspace(item):
            picture = cv.imread(f"{to_path}\{item}.jpg")

            gray = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
            cv.imwrite(f"{item}1.jpg", gray)

            blur = cv.GaussianBlur(picture, (5,5), cv.BORDER_DEFAULT)
            cv.imwrite(f"{item}2.jpg", blur)

            rgb = cv.cvtColor(picture, cv.COLOR_BGR2RGB)
            cv.imwrite(f"{item}3.jpg", rgb)
        
        img = cv.imread(f"{student_name}.jpg")
        
        p1 = int(img.shape[1]*0.25)
        p2 = int(img.shape[0]*0.25)

        translated1 = translate(img, -p1, p2)
        cv.imwrite("T1.jpg", translated1)

        translated2 = translate(img, p1, p2)
        cv.imwrite("T2.jpg", translated2)

        translated3 = translate(img, p1, -p2)
        cv.imwrite("T3.jpg", translated3)

        translated4 = translate(img, -p1, -p2)
        cv.imwrite("T4.jpg", translated4)

        pic_list = [f"{student_name}", "T1", "T2", "T3", "T4"]

        for item in pic_list:
            change_clrspace(item)