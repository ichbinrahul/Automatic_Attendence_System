from train import Trainer
from register import Register
from attendence_marker import Marker
import os
import time

def loop_function():
    try:
        os.system("cls")
        print("\nOpenCV based Attendence System\n")
        choice = int(input("\n1 > Start Session\n2 > Manage Data\nAnyother integer > Exit\n\nYour Choice >> "))
        if choice == 1:
            os.system("cls")
            print("Attendence Session")
            try:
                attendence = Marker()
                if attendence:
                    print("\n")
                    attendence.start_session()
            except TypeError:
                print("\nPlease check the entered class exists, or you have trained the model for the class.\n")
            time.sleep(5)
            loop_function()
        elif choice == 2:
            os.system("cls")
            print("\nManage Data\n")
            second_choice = int(input("\n1 > Add or Edit Student\n2 > Train model\n3 > Back to Main Menu\nAnyother integer > Exit Program\n\nYour Choice >> "))
            if second_choice == 1:
                os.system("cls")
                print("\nAdd or Edit Student\n")
                try:
                    os.mkdir("Class-List")
                except FileExistsError:
                    pass
                manage_student = Register()
                manage_student.make_dir()
                while(True):
                    manage_student.capture_image()
                    if input("\nDo you want to add more students ('n' to exit) >> ") == "n":
                        print("\nAll Done...........\n")
                        break
                time.sleep(5)
                loop_function()
            elif second_choice == 2:
                os.system("cls")
                print("\nTrain Model\n")
                train_model = Trainer(input("\nEnter Class >> "))
                print("\nTraining Started. This may take some time....\n")
                train_model.start_trainer()
                time.sleep(5)
                loop_function()
            elif second_choice == 3:
                loop_function()
        elif choice == 3:
            exit()
    except ValueError:
        print("\nPlease enter a valid choice")
        time.sleep(3)
        loop_function()

loop_function()