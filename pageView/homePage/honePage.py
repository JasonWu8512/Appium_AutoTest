import time

import allure
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pageView.basePage import BasePage
from data.testData import HomePageData


class HomePage(BasePage):
    alwaysAllow_btn1 = HomePageData.alwaysAllow_btn1
    alwaysAllow_btn2 = HomePageData.alwaysAllow_btn2
    limitedTime_btn1 = HomePageData.limitedTime_btn1
    limitedTime_btn2 = HomePageData.limitedTime_btn2

    def home(self):
        with allure.step("首页，通知权限"):
            try:
                self.click_element(*self.alwaysAllow_btn1, doc="通知权限，始终允许")
            finally:
                self.click_element(*self.alwaysAllow_btn2, doc="通知权限，始终允许")

        time.sleep(3)
        with allure.step("首页，领取banner/icon"):
            try:
                self.click_element(*self.limitedTime_btn1, doc="限时领取banner")
            finally:
                self.click_element(*self.limitedTime_btn2, doc="限时领取icon")

    def home_swipe_down(self, driver):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(704, 544)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(676, 1617)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
