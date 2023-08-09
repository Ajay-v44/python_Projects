#for mac os
# import os
# if __name__=='__main__':
#     print("welcome to RoboSpeaker 2.0 ")
#     speech=input("Enter what you want  me to pronounce\t")
#     command= f"say {speech}"
#     os.system(command)

import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.0")
    speech = input("Enter what you want me to pronounce: ")


    engine = pyttsx3.init()


    engine.say(speech)
    engine.runAndWait()
