from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
from webdriver_manager import driver
from Config.config import Testdata
from Pages.BasePage import BasePage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class StartPage(BasePage):
    start_time_input = (By.ID, "EggTimer-start-time-input-text")
    Start_button = (By.XPATH, "//button[contains(text(),'Start')]")
    Five_MIN = (By.LINK_TEXT, "/5 minutes")
    Ten_MIN = (By.LINK_TEXT, "/10 minutes")
    Fifteen_MIN = (By.LINK_TEXT, "/15 minutes")
    Help_Text = (By.XPATH, "//button[normalize-space()='Help and Settings']")
    EGG_Timer_Twitter = (By.XPATH, "//a[normalize-space()='@edotggtimer']")
    PomoDoro = (By.XPATH, "//a[normalize-space()='/Pomodoro']")
    Tabata = (By.XPATH, "//a[normalize-space()='/Tabata']")
    Morning = (By.XPATH, "//a[normalize-space()='/Morning']")
    Welcome_Msg = (By.XPATH, "//div[@class='EggTimer-start-welcome']")
    countdown = (By.XPATH, "//span")
    """Constructor Of the Page Class"""

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)
        self.driver.get('https://e.ggtimer.com/')

    """Page Actions for Start Page """

    """This is used to get the title of the Page"""

    def get_title_start_page(self, title):
        print(self.get_title(title))
        return self.get_title(title)

    """This is used to send Enter the time and click Start"""

    def enter_the_time(self, timeinseconds):
        self.send_key(self.start_time_input, timeinseconds)
        self.do_click(self.Start_button)
        print("click happened")
        time.sleep(3)

    def count_down_timer(self):
        print(self.driver.title)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_id("EggTimer-start-time-input-text").send_keys(25)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()
        time.sleep(2)
        before = "None"
        after = "None"
        while True:
            after = self.driver.find_element_by_xpath("//span").text
            time.sleep(1)
            if after != before:
                print("after value", after)
                before = after
                print("before value", before)
                if before == "0 second":
                    break

        time.sleep(2)
        alert = Alert(self.driver)
        alert.accept()
        #timeout_expired = self.driver.find_element_by_xpath("//span").text
        print("Countdown Completed")
        #if before == timeout_expired:
        #    print("Countdown Completed")
        self.driver.get('https://e.ggtimer.com/')

