import webbrowser #?import browser module
class Webber():#?create a class for 
    def __init__(self):
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None ,webbrowser.BackgroundBrowser(chrome_path))
        self.browser = webbrowser.get('chrome') 
    def openURL(self, URL):
        self.browser.open(URL)




# chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# webbrowser.register('chrome', None ,webbrowser.BackgroundBrowser(chrome_path))
# web = webbrowser.get('chrome')
# web.open("youtube.com")