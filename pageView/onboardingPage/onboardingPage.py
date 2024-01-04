import allure

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from pageView.basePage import BasePage
from data.testData import OnboardingPageData


class OnboardingPage(BasePage):
    # 按钮元素定位
    home_tab_btn = OnboardingPageData.home_tab_btn
    agree_btn = OnboardingPageData.agree_btn
    secret_login_btn = OnboardingPageData.secret_login_btn
    pw_login_btn = OnboardingPageData.pw_login_btn
    checkBox_btn = OnboardingPageData.checkBox_btn
    more_btn = OnboardingPageData.more_btn
    youke_btn = OnboardingPageData.youke_btn
    startLearn_btn = OnboardingPageData.startLearn_btn
    limitedTime_btn1 = OnboardingPageData.limitedTime_btn1
    limitedTime_btn2 = OnboardingPageData.limitedTime_btn2
    limitedTime__close_btn3 = OnboardingPageData.limitedTime__close_btn3
    level_change_btn = OnboardingPageData.level_change_btn

    # 输入框&文本定位
    mobile_input = OnboardingPageData.mobile_input
    pw_input = OnboardingPageData.pw_input
    schedule_text = OnboardingPageData.schedule_text
    year_level_title_text = OnboardingPageData.year_level_title_text
    level_title_text = OnboardingPageData.level_title_text

    # 通知权限
    alwaysAllow_btn1 = OnboardingPageData.alwaysAllow_btn1
    alwaysAllow_btn2 = OnboardingPageData.alwaysAllow_btn2

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.limitedTime_btn1 = (MobileBy.ID, 'com.jiliguala.niuwa:id/showImage')

    # 游客用户
    def guestLogin(self):
        with allure.step("启动页，点击同意按钮"):
            self.click_element(*self.agree_btn, doc="同意按钮")
        with allure.step("登录页，点击密码登录"):
            self.click_element(*self.secret_login_btn, doc="密码登录")
        with allure.step("登录页，勾选同意"):
            self.click_element(*self.checkBox_btn, doc="勾选同意")
        with allure.step("登录页，点击更多"):
            self.click_element(*self.more_btn, doc="更多")
        with allure.step("登录页，点击游客试用"):
            self.click_element(*self.youke_btn, doc="游客试用")
        with allure.step("宝贝年龄页，点击开始学习"):
            self.click_element(*self.startLearn_btn, doc="开始学习")
        with allure.step("首页，通知权限"):
            try:
                self.click_element(*self.alwaysAllow_btn1, doc="通知权限，始终允许")
            finally:
                self.click_element(*self.alwaysAllow_btn2, doc="通知权限，始终允许")
        with allure.step("首页，关闭领取banner"):
            try:
                self.click_element(*self.limitedTime__close_btn3, doc="关闭领取banner")
            finally:
                pass

    def login_with_credentials(self, username, password):
        with allure.step("启动页，点击同意按钮"):
            self.click_element(*self.agree_btn, doc="同意按钮")
        with allure.step("登录页，点击密码登录"):
            self.click_element(*self.secret_login_btn, doc="密码登录")
        with allure.step("登录页，点击手机号输入框，并输入手机号/邮箱"):
            self.click_element(*self.mobile_input, doc="手机号输入框")
            self.send_keys(*self.mobile_input, value=username, doc="手机号输入框")
        with allure.step("登录页，点击密码输入框，并输入密码"):
            self.click_element(*self.pw_input, doc="密码输入框")
            self.send_keys(*self.pw_input, value=password, doc="密码输入框")
        with allure.step("登录页，勾选同意"):
            self.click_element(*self.checkBox_btn, doc="勾选同意")
        with allure.step("登录页，点击登录按钮"):
            self.click_element(*self.pw_login_btn, doc="登录按钮")

    # 已购年课正价课用户
    def y_user_pwLogin(self):
        with allure.step("年课用户登录"):
            self.login_with_credentials(username="nktest@2.com", password="123456")

    #  无购买用户
    def no_pay_user_pwLogin(self):
        with allure.step("无购买用户登录"):
            self.login_with_credentials(username="11100001112", password="Qweasd@123")

    # 已购88用户
    def pay_88_user_pwLogin(self):
        with allure.step("已购88用户登录"):
            self.login_with_credentials(username="11100001113", password="Qweasd@123")

    def home_popup_close(self):
        with allure.step("等待首页弹窗出现"):
            return self.is_element_exist(*self.limitedTime_btn2, doc="限时领取")

    def get_home_notification(self):
        with allure.step("首页，通知权限"):
            try:
                self.click_element(*self.alwaysAllow_btn1, doc="通知权限，始终允许")
            finally:
                self.click_element(*self.alwaysAllow_btn2, doc="通知权限，始终允许")

    def get_home_banner(self):
        with allure.step("首页，领取banner/icon"):
            try:
                self.click_element(*self.limitedTime_btn1, doc="限时领取banner")
            finally:
                self.click_element(*self.limitedTime_btn2, doc="限时领取icon")

    def close_home_banner(self):
        with allure.step("首页，关闭领取banner"):
            try:
                self.click_element(*self.limitedTime__close_btn3, doc="关闭领取banner")
            finally:
                pass

    def get_level_title_text(self):
        with allure.step("等待首页按钮出现"):
            return self.get_text(*self.level_title_text, doc="获取级别")

    def get_year_level_title_text(self):
        with allure.step("等待文本出现"):
            return self.get_text(*self.year_level_title_text, doc="获取级别")

    def open_level_change(self):
        print("*self.level_change_btn:", *self.level_change_btn)
        with allure.step("点击切换级别"):
            self.click_element(*self.level_change_btn, doc="切换级别")

