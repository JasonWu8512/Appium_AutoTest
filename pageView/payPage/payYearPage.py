import allure

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from pageView.basePage import BasePage
from data.testData import PayPageData


class PayYearPage(BasePage):
    pay_tab_btn = PayPageData.pay_tab_btn
