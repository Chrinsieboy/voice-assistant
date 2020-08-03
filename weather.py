import requests # Importing requests module to request from the weather API
import json # Importing JSON module to parse data from the requests




class Weather():
    def __init__(self, API_KEY="API-KEY-FROM-CONFIG.JSON"): # Request the api key in the constractor
        self.API_KEY = API_KEY 
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?" # Base URL of the API
        
    
    def getWeather(self, CITY): #? Defining a function to get the current weather from a CITY parameter
        URL = f"{self.BASE_URL}q={CITY}&appid={self.API_KEY}&units=metric" # Building the new URL with our API key and CITY parameter
        response = requests.get(URL) # Trying to connect the url w/ requests module
        if response.status_code == 200: #? Checking if we connected successfully (code 200)
            data = response.json() # Parse the data from JSON to Python dictionary
            
            main = data['main'] # Getting the main dict block
            temperature = main['temp']  # Getting temperature
            feels_like = main['feels_like'] # Getting the "feels like" temperature
            humidity = main['humidity'] # Getting the humidity
            pressure = main['pressure' ] # Getting the pressure
            report = data['weather'] # Getting eather report by words

            #* Printing the data we need:
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Pressure: {pressure}")
            print(f"Weather Report: {report[0]['description']}")           
            return (f"The temprature is {temperature} celcius in {CITY}, but feels like {feels_like} ")
        
            
        else: #? If the code isn't 200, such as 400, 401, 403, 404...
            print("Error in the HTTP request")
            print(response.status_code)
        



    
    

