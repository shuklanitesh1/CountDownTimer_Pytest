import time

import pytest
from selenium.webdriver.common.by import By

from Config.config import Testdata
from Pages.StartPage import StartPage
from Test.test_base import BaseTest


# @pytest.mark.usefixtures["init_driver"]  # fixture can be directly used like this as well
class Test_Egg_Timer(BaseTest):

    def test_countdown_timer(self):
        self.verifytimer = StartPage(self.driver)
        self.verifytimer.count_down_timer()
        #StartPage.demo_heck_boxes(self)
        self.driver.implicitly_wait(3)
