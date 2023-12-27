import pyfirmata2
import time
import speech_recognition as sr 
import pyaudio
import pywhatkit

from gtts import gTTS


board = pyfirmata2.Arduino("COM4")
redpin = board.get_pin("d:3:o")
greenpin = board.get_pin("d:4:o")
bluepin = board.get_pin("d:5:o")
while True:
    print("rec..")
    l = sr.Recognizer()
    with sr.Microphone() as mic:
        voice = l.listen(mic)
        com = l.recognize_google(voice)
        com = com.lower()

        print(com)

        if com=="computer red":
            redpin.write(0) #that values for common anode rgb led
            
            greenpin.write(1)
            bluepin.write(1)

        elif com=="computer green":
            greenpin.write(0)
            redpin.write(1)
            
            bluepin.write(1)

        elif com=="computer blue":
            bluepin.write(0)
            redpin.write(1)
            greenpin.write(1)
        elif com=="computer on":
            greenpin.write(0)
            redpin.write(0)
            
            bluepin.write(0)

        elif com=="computer off":
            redpin.write(1)
            greenpin.write(1)
            bluepin.write(1)
        elif com=="computer exit":
            break
        else:
            print("try again")
board.exit()
