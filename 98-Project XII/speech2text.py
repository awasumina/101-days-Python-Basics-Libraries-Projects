# pip install SpeechRecognition
# pip install pyaudio

import pyttsx3
import speech_recognition as sr

def get_audio() :
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please say something!")
        audio = r.listen(source)
        print("DONE!!")
        
    try:
        text = r.recognize_google(audio)
        print("You said : "+ text)
    
    except Exception as e:
        print('Sorry, I did not understand')
        # print(e)
        
get_audio()