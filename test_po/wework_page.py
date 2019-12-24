from time import sleep

from selenium import webdriver


class Wework:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        self.driver.get(url)
        cookie = {"wwrtx.i18n_lan": "zh",
                  "wwrtx.d2st": "a1821743",
                  "wwrtx.sid": "fyDmugfJ4e01ULqCxU1emKHGMfG1VHO8p_X0XbN-5U4bgjzmYna_BdY5j3zncFI5",
                  "wwrtx.ltype": "1",
                  "wxpay.corpid": "1970324980092056",
                  "wxpay.vid": "1688850754733339"}
        for k, v in cookie.items():
            self.driver.add_cookie({"name": k, "value": v})
            self.driver.get(url)

    def quit(self):
        # self.driver.quit()
        sleep(4)