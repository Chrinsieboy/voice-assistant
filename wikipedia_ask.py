import wikipedia # Importing wikipedia module

class Wikipedia(): # Creating a class for every wiki page
    def getSummary(self, value, detailed): #? func that creates 
         # Checking if the user wants detailed info
        if detailed == 'NO':
            sen_len = 1
        elif detailed == 'YES':
            sen_len = 4

        text = wikipedia.summary(value, sentences = sen_len) # Creating text varible that includes wiki page summary 

        return text # Returning the summary

