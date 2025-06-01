import configparser

# config= None
config = configparser.ConfigParser()
config.read("../../config.ini")
class baseClass():




    def __init__(self):
        global  config

        self.driver= config.get("app","browser")
        print('the driver from base class is '+self.driver)



    def initialiseBrowser(self):
        print("My driver from BaseClass :" + self.driver)
        return self.driver
# a= baseClass()
# a.initialiseBrowser()