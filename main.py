# importing requests and json
from weather import weather
from capital import makeCapital
import speech_recognition as sr
# base URL

    

r = sr.Recognizer()

with sr.Microphone() as source:
    print("What city do you want to check the weather for?\n")
    audio = r.listen(source)

    try:
        #language = 'he-IL'
        text = r.recognize_google(audio)
        text = makeCapital(text)
        weather(text)
    except Exception as e:
        print("Sorry, I could not recognize your voice")
        print(e)
