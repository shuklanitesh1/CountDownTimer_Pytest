import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import Testdata


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    # global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--disable-notifications")
        # web_driver = webdriver.Chrome(executable_path=Testdata.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        #web_driver = webdriver.Chrome(GeckoDriverManager().install())
        web_driver = webdriver.Chrome(executable_path=Testdata.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
