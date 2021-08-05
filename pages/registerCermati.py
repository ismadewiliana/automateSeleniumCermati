import time
from selenium.webdriver.common.by import By

class registerNewAccount():

    def __init__(self, driver):
        self.driver = driver

    def inputDataRegister(self):

        # Wait for 3 sec
        time.sleep(3)

        # Input email address
        emailaddress = self.driver.find_element(By.ID, "email")
        emailaddress.send_keys("ismadewiliana@gmail.com")

        # Input password
        passwordset = self.driver.find_element(By.NAME, "password")
        passwordset.send_keys("rah@sianegara1234")

        # Input confirm password
        confirmpass = self.driver.find_element(By.ID, "confirm-password")
        confirmpass.send_keys("rah@sianegara1234")

        # Input first name
        firstname = self.driver.find_element(By.XPATH, "//input[@id='first-name']")
        firstname.send_keys("Isma Dewi")

        # Input last name
        lastname = self.driver.find_element(By.ID, "last-name")
        lastname.send_keys("Liana")

        # Input mobile phone number
        mobilephone = self.driver.find_element(By.ID, "mobile-phone")
        mobilephone.send_keys("081264935957")

        # Input Recidence City
        residence = self.driver.find_element(By.ID, "residence-city")
        residence.send_keys("Jakarta")

        # Choose the Recidence City
        city = self.driver.find_element(By.XPATH, "//div[contains(text(), 'KOTA JAKARTA BARAT')]")
        city.click()

        # # Click register button
        # resgisterbutton = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Daftar Akun' )]")
        # resgisterbutton.click()