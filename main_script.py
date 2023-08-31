import os
from pathlib import Path
import sys
import subprocess

os.chdir(Path(__file__).parent.absolute())

def print_menu():
    print("Select a script to run:")
    print("1. Dataset Creation")
    print("2. Preprocessing Embeddings")
    print("3. Training Face ML")
    print("4. Recognizing Person")
    print("5. Recognizing Person with CSV dataset")
    print("0. Exit")

def run_script(script_number):
    if script_number == 1:
        subprocess.run([sys.executable,"1_datasetCreation.py"],shell=True)
    elif script_number == 2:
        subprocess.run([sys.executable,"2_preprocessingEmbeddings.py"],shell=True)
    elif script_number == 3:
        subprocess.run([sys.executable,"3_trainingFaceML.py"],shell=True)
    elif script_number == 4:
        subprocess.run([sys.executable,"4_recognizingPerson.py"],shell=True)
    elif script_number == 5:
        subprocess.run([sys.executable,"5_recognizingPersonwithCSVDatabase.py"],shell=True)
    else:
        print("Invalid choice.")

def main():
    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice (1-5, or 0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= 5:
                run_script(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
