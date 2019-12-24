from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import Basepage
from test_po.profile_page import ProfilePage


class ContactPage(Basepage):
    _addmember=(By.CSS_SELECTOR, '.js_has_member .js_add_member')
    _username=(By.NAME, "username")
    _acctid=(By.NAME, "acctid")
    _email=(By.NAME, "alias")
    _picture=(By.CSS_SELECTOR, "#js_upload_file .ww_icon_CameraWhiteSmall")
    _picture1=(By.CSS_SELECTOR, ".js_no_img.cropper_noImage > a > input")
    _save=(By.CSS_SELECTOR, ".js_save")

    def __init__(self,Wework):
        self.driver=Wework.driver
    def add_menber(self, name, alias, email,picture,**kwargs):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_has_member .js_add_member')))
        self.click_script(*self._addmember)
        self.driver.find_element(*self._username).send_keys(name)
        self.driver.find_element(*self._acctid).send_keys(alias)
        self.driver.find_element(*self._email).send_keys(email)

        # 上传图片
        self.driver.find_element(*self._picture).click()

        self.driver.find_element(*self._picture1) \
            .send_keys(picture)
        # print(self.driver.page_source)
        # assert "重新上传" in self.driver.page_source
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((
            By.CSS_SELECTOR, ".js_file_reupload")))

        self.driver.find_element(*self._save).click()

        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((
        #     By.CSS_SELECTOR, ".js_btn_save")))
        # self.driver.execute_script("window.scrollBy(0,300)")#下滑界面
        # self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        self.click_script(By.CSS_SELECTOR, ".js_btn_save")


    def delet_menber(self):
        pass
    def get_tips(self):
        return "ok"
    def search(self,key):
        self.driver.find_element(By.ID,"memberSearchInput").send_keys(key)
        return ProfilePage(self.driver)

    def click_script(self,by_key,locat):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by_key,locat))


