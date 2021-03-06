from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    def __init__(self,driver:WebDriver):
        self.driver=driver
    def click_script(self,by_key,locat):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((by_key,locat)))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by_key,locat))

