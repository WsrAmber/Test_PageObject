from time import sleep, time

from selenium import webdriver

from test_po.contact_page import ContactPage
from test_po.wework_page import Wework


class TestContact:
    def setup(self):
        self.work=Wework()
        self.contact=ContactPage(self.work)

    def teardown(self):
        self.work.quit()

    def test_add_menber(self):
        self.contact.add_menber("namesdaff","aliasasss","aliasss5sdg@qq.com1","D:\IMAGE\images.jpg")
        assert self.contact.get_tips() =="ok"

    def test_delete(self):
        udid=str(time())
        self.contact.add_menber("name"+udid,"asdasf"+udid,"sdasfas@qq.com"+udid,"picture").delet_menber()

    def test_update_profile(self):
        self.contact.search("name").update(name="name %s" % str(time()))
