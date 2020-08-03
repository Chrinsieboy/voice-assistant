from datetime import datetime # Importing datetime class from datetime module to get the current time

class Date():
    def getTime(self): # Creating a function to get the current time
        dateToday = datetime.now() # Creating an instance of datetime.now() to get the time

        self.times = {
            'year' : dateToday.strftime("%Y"),  # Get current year
            'month_num' : dateToday.strftime("%m"), # Get current month by number
            'month_name' : dateToday.strftime("%B"), # Get current month by name
            'day_num' : dateToday.strftime("%#d"), # Get current day of month by number
            'day_name' : dateToday.strftime("%A"), # Get current day by name
            'hour_num' : dateToday.strftime("%H"), # Get current hour by number
            'hour_num_24' : dateToday.strftime("%#H"), # Get current hour by number without zero's (08 = 8, for Jarvis to read properly)
            'hour_name' : dateToday.strftime("%#I%p"), # Get current hour without zeros and by adding timezone (AM\PM)
            'minute_num' : dateToday.strftime("%M"), # Get current minute by number
            'minute_name' : dateToday.strftime("%#M"), # Get current minute be number without zeros (08 = 8, for Jarvis to read properly)
            'second_num' : dateToday.strftime("%S"), # Get current second by number
            'second_name' : dateToday.strftime("%#S") # Get current second by number without zeros (08 = 8, for Jarvis to read properly)
        }

        return self.times # Return the current time dictionary
        
    def getBless(self): # Get the bless for Jarvis to bless depends on the current time
        self.times = self.getTime() # Getting the current time
        if int(self.times['hour_num_24']) in range(4, 12): #? Checking if its morning
            return "good morning"
        elif int(self.times['hour_num_24']) in range(12, 18): #? Checking if its afternoon
            return "good afternoon"
        elif int(self.times['hour_num_24']) in range(18, 21): #? Checking if its evening
            return "good evening"
        elif int(self.times['hour_num_24']) in range(21, 24) or int(self.times['hour_num_24']) in range(0, 4): # Checing if its night
            return "good night"
        
   
    def getStartUpDate(self): #? Get the sentence for Jarvis to start up
        self.times = self.getTime()
        return f"Today is {self.times['day_name']}, {self.times['month_name']} {self.times['day_num']}"
            

    def getHourByName(self): #? Get the current hour for Jarvis to read properly
        self.times = self.getTime()
        return f"It's {self.times['hour_name']} and {self.times['minute_name']} minutes"


# date = Date()
# date.getTime()
# for i in range(5 ,12):
#     print(i)
#     date.times['hour_num_24'] = i
#     print(date.getBless())





