# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class jira(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_jira(self):
        success = True
        wd = self.wd
        wd.get("https://jira.wiley.ru/secure/Dashboard.jspa")
        wd.find_element_by_id("login-form-username").click()
        wd.find_element_by_id("login-form-username").send_keys("\\undefined")
        wd.find_element_by_id("login-form-password").click()
        wd.find_element_by_id("login-form-password").send_keys("\\undefined")
        wd.find_element_by_id("login").click()
        wd.find_element_by_id("find_link").click()
        wd.find_element_by_id("issue_lnk_211421_lnk").click()
        wd.find_element_by_id("summary-val").click()
        wd.find_element_by_id("summary").click()
        wd.find_element_by_css_selector("button.aui-button.submit").click()
        wd.find_element_by_xpath("//div[@class='user-content-block']//p[.='No database changes.']").click()
        wd.find_element_by_css_selector("button.aui-button.submit").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
