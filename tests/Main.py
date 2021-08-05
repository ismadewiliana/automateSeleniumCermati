import time
import unittest
from selenium import webdriver
from pages.registerCermati import registerNewAccount


class mainTest(unittest.TestCase):

    def test_registerCermati(self):
        url = "https://www.cermati.com/gabung"
        driver = webdriver.Chrome() #Open Chrome Browser
        driver.maximize_window() #Maximize the chrome browser
        driver.implicitly_wait(3) #Wait for 3 sec
        driver.get(url) #Navigate the url

        rc =  registerNewAccount(driver)
        rc.inputDataRegister()
        print("Success input data register new account")

        time.sleep(5)

        driver.quit()

mt = mainTest()
mt.test_registerCermati()