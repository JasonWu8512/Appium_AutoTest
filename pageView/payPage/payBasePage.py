import allure

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from pageView.basePage import BasePage
from data.testData import PayPageData


class PayBasePage(BasePage):
    pay_tab_btn = PayPageData.pay_tab_btn
    pay_btn = PayPageData.pay_btn
    pay_how_use_btn = PayPageData.pay_how_use_btn
    pay_back_btn1 = PayPageData.pay_back_btn1
    pay_back_btn2 = PayPageData.pay_back_btn2

    pay_how_use_text = PayPageData.pay_how_use_text

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def payTab(self):
        with allure.step("首页，点击购买tab"):
            self.click_element(*self.pay_tab_btn, doc="购买tab")

    def pay_how_use(self):
        with allure.step("购买页，点击如何使用"):
            self.click_element(*self.pay_how_use_btn, doc="如何使用")

    def payBack(self):
        with allure.step("购买页，点击返回"):
            self.click_element(*self.pay_back_btn1, doc="返回")

    def payActionBack(self):
        with allure.step("如何使用，点击返回"):
            self.click_element(*self.pay_back_btn2, doc="返回")

    def get_pay_how_use_text(self):
        with allure.step("等待页面出现"):
            return self.is_element_exist(*self.pay_how_use_text, doc="如何使用")

    def pay_swipe_up(self, driver):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(676, 2848)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(720, 880)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
