from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from random import randint
import time
import sys
from tkinter import *


class Bot:


    window = Tk()

    driver_width = 500
    driver_height = 400

    driver = webdriver.Chrome()
    x = 0

    def joinGame(self, name, game_gen_id):

        driver = self.driver

        driver.get("https://kahoot.it/#/")
        time.sleep(4)

        inputSession = driver.find_element_by_xpath('//*[@id="inputSession"]')
        inputSession.send_keys(str(game_gen_id))
        driver.find_element_by_xpath('//*[@id="mainView"]/div/div/div/form/button').click()
        time.sleep(4)

        name = driver.find_element_by_xpath('//*[@id="username"]')
        name.send_keys("Teo")
        driver.find_element_by_xpath('//*[@id="mainView"]/div/div/div/form/button').click()
        time.sleep(4)

    def playGame(self, choices, times):

        x = 0

        self.driver.switch_to.frame("gameBlockIframe")

        answered = False


        while 1:

            try:
                self.driver.find_element_by_xpath('//*[@id="app"]/main/div/button[1]')


                try:

                    print("Trying")
                    button_path = '//*[@id="app"]/main/div/button[' + str(int(choices[x] + 1)) + ']'
                    print(button_path)
                    self.driver.find_element_by_xpath(button_path).click()
                    print("Question Answered: " + str(x))
                    answered = True
                    x += 1
                except Exception as e:
                    print("waiting")

            except NoSuchElementException:
                print("Trying Again")


        time.sleep(.01)



            #//*[@id="app"]/main/div/button[1]
            #//*[@id="app"]/main/div/button[2]
            # //*[@id="app"]/main/div/button[3]
            # //*[@id="app"]/main/div/button[4]

    def doesExist(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

