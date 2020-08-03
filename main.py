from weather import Weather # Importing the weather py to check out the current weather
from capital import makeCapital # Importing capital py that makes things more beautiful by capitalizing them
import speech_recognition as sr # Importing the module that can listen and understand what the user says
import pyttsx3 # Importing the module that can speak to the user
import json # Importing JSON module that has config for the program
from wikipedia_ask import Wikipedia # Importing wiki.py for getting wiki page summary
from date import Date # Importing date.py module to get date information
from time import sleep # Importing time.sleep to add a delay
from web_open import Webber # Importing Webber class to be able to search and open web browsers
from commands import commands, sorry_list # Importing the commands Jarvis supports, and the list for Jarvis when he doesn't understand
import random # Importing random library to select random answers for Jarvis



class Assistant(Weather, Wikipedia, Date, Webber): #! Jarvis class
    def __init__(self, config):
        super().__init__() # Getting all the commands constractors
        self.setConfig(config) # Setting the config for Jarvis
        self.Recognizer = sr.Recognizer() # Custom Recognizer
        self.Microphone = sr.Microphone() # Custom Microphone
        self.engine = pyttsx3.init() # Custom Engine
        self.commands = commands

        #* Setting config for the Engine:
        self.setGender()
        self.setVolume()
        self.setSpeedRate()

        #* Setting up objects from the super classes:
        self.date = Date()
        self.weather = Weather()
        self.wiki = Wikipedia()
        self.web = Webber()
    
    def setConfig(self, config):
        self.name = config['name']
        self.city = config['city']
        self.volume = config['volume']
        self.gender = config['gender']
        self.speedRate = config['speedRate']
    
    def setVolume(self):
        self.engine.setProperty('volume', self.volume)

    def setGender(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.gender].id)
    
    def setSpeedRate(self):
        self.engine.setProperty('rate', self.speedRate)



    def listen(self):
        with self.Microphone as source:
            try:
                print("I'm listening...")
                audio = self.Recognizer.listen(source)
                text = self.Recognizer.recognize_google(audio)
                return text
            except:
                return f"Sorry {self.name}, I couldn't hear you."

    def say(self, whatToSay):
        self.engine.say(whatToSay)
        self.engine.runAndWait()

    def recognize(self, text):
        #if text.lower() in self.commands:
        text = text.lower() 
        if 'weather in' in text:
            textSplitted = text.split()
            print(textSplitted[len(textSplitted) - 1])
            return self.weather.getWeather(textSplitted[len(textSplitted) - 1])
        elif 'weather' in text:
            return self.weather.getWeather(self.city)
        elif "your name" in text:
            return "Jarvis, Sir"    
        elif "my name" in text:
            return self.name + " the king"
        elif "year" in text or "ear" in text:
            return self.date.getTime()['year']
        elif "the time" in text:
            return self.date.getHourByName()
        elif "open" in text:
            if "youtube" in text:
                self.web.openURL("youtube.com")
            elif "google" in text:
                self.web.openURL("google.com")    
            elif "stack overflow" in text:
                self.web.openURL("stackoverflow.com")
            else:
                self.say("I'm not skilled enough to open this")
        elif "wiki" in text or "wikipedia" in text or "what is" in text:
            self.say("what is the subject that you want to know?")
            text = self.listen()
            if 'close' in text or 'exit' in text or 'leave' in text or 'back' in text or 'nothing' in text:
                pass
            else:
                print(self.getSummary(text, 'NO'))               
        else:
            return random.choice(sorry_list)
            


    def startUp(self):
        bless = self.getBless()
        self.say(f"Hi {self.name}, {bless}")
        print(bless)      
        self.say(self.getStartUpDate())

    
        

        


with open('config.json', 'r') as con:
    config = json.load(con)


Jarvis = Assistant(config)

Jarvis.startUp()
x = Jarvis.listen()
print(x)
data = Jarvis.recognize(x)
Jarvis.say(data)




