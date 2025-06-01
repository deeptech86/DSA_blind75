import unittest

from src.baseClass import baseClass
from src.pages.homepage import homepage


class testhomepage(baseClass):
    def __init__(self, driver):
        super().__init__()
        self.driver=driver

    def firsttest(self):
        # baseClass.initialiseBrowser(self.driver)
        homepage.newZipCode(self)
        print('test homepage is '+ self.driver)


driver="chromedriver"
a= testhomepage(driver)

a.firsttest()