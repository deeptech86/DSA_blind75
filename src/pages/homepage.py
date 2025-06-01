from self import self

from src.baseClass import baseClass


class homepage(baseClass):

    def __init__(self,driver):


        super().__init__()
        self.driver=driver

    def newZipCode(self):
        # baseClass.initialiseBrowser(self)
        print("this is the driver from homepage : "+self.driver)


# a=homepage("sas")
# a.newZipCode()
# a.initialiseBrowser()

