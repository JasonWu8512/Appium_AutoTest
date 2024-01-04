import allure

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from pageView.basePage import BasePage
from data.testData import PayPageData


class GuestPayPage(BasePage):
    pw_login_link = PayPageData.pw_login_link
    pw_login_btn = PayPageData.pw_login_btn
    limitedTime_btn1 = PayPageData.limitedTime_btn1
    limitedTime_btn2 = PayPageData.limitedTime_btn2
    banner_group_btn1 = PayPageData.banner_group_btn1
    banner_group_btn2 = PayPageData.banner_group_btn2
    banner_group_btn3 = PayPageData.banner_group_btn3
    banner_group_btn4 = PayPageData.banner_group_btn4
    banner_group_btn5 = PayPageData.banner_group_btn5

    parent_lock_text = PayPageData.parent_lock_text
    pay_title_text = PayPageData.pay_title_text
    pay_price_text = PayPageData.pay_price_text

    mobile_input = PayPageData.mobile_input
    pw_input = PayPageData.pw_input

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def guestPayBanner(self):
        with allure.step("首页，点击0元英语启蒙体验营banner"):
            self.click_element(*self.banner_group_btn1, doc="0元英语启蒙体验营")
            return self.get_texts(self.pay_title_text, self.pay_price_text, doc="获取标题和价格")

