import pyttsx3
import os

engine = pyttsx3.init()

num = 1
name = "tts"
string = "ENTER YOUR STRING"

engine.save_to_file(string, "(" + str(num) + ") " + name + ".mp3")
engine.runAndWait()

source = "(" + str(num) + ") " + name + ".mp3"
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
            os.replace(source, destination + source)
            print(source + " was moved")
    except FileNotFoundError:
        print(source + " was not found")

def checkExists(index):
    path = destination + "(" + str(index) + ") " + name + ".mp3"
    if(os.path.exists(path)):
        return True
    else:
        return False

moveFile()
