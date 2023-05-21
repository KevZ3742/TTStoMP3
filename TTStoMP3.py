import pyttsx3
import os

engine = pyttsx3.init()

# Dont touch, this var deals with duplicate names
num = 1
# Change this to your desired name
name = "tts"

# Changed this to yout desired output
string = "ENTER YOUR STRING"

engine.save_to_file(string, "(" + str(num) + ") " + name + ".mp3")
engine.runAndWait()

source = "(" + str(num) + ") " + name + ".mp3"
# Change this to your desired save location
destination = "C:\\Users\\Kevin Zhang\\Videos\\TTS\\"

def moveFile():
    try:
        if(os.path.exists(destination + source)):
            action = input("File already exists (Override: o, Keep Both: k, Quit: q): ")

            if(action == "o"):
                os.replace(source, destination + source)
                print(source + " was moved")
            elif(action == "k"):
                i = 1
                while(checkExists(i)):
                    i += 1
                num = i
                os.replace(source, destination + "(" + str(num) + ") " + name + ".mp3")
                print(source + " was moved")
            elif(action == "q"):
                exit()
            else:
                print("Invalid input")
                exit()
        else:
            os.replace(source, destination + source)
            print(source + " was moved")
    except FileNotFoundError:
        print(source + " was not found")

# Checks if a path exists
def checkExists(index):
    path = destination + "(" + str(index) + ") " + name + ".mp3"
    if(os.path.exists(path)):
        return True
    else:
        return False

moveFile()