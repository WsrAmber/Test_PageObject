from time import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import Basepage


class ProfilePage(Basepage):
    def update(self,**kwargs):
        self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_edit").click()
        element=self.driver.find_element(By.NAME,"username")
        element.clear()
        element.send_keys(kwargs["name"])
        self.click_script(By.CSS_SELECTOR,".ww_operationBar .js_save")

    def Disable(self):
        pass
    def Startup(self):
        pass
